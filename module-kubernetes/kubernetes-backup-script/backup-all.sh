#!/bin/bash

RESOURCES=(deployments services configmaps secrets namespaces)
IGNORED_NAMESPACES=(kube-system kube-public kube-node-leases)
BACKUP_DIR=/tmp/k8s-backup

mkdir -p $BACKUP_DIR

# Loop que percorre todos os namespaces
for ns in $(kubectl get namespaces -o jsonpath='{.items[*].metadata.name}'); do
  # Pula o namespace ignorado
  if [[ "${IGNORED_NAMESPACES[@]}" =~ "${ns}" ]]; then
    echo "[ ! ] ignoring namespace $ns"
    continue
  fi

  ns_backup_dir="$BACKUP_DIR/$ns"
  mkdir -p $ns_backup_dir

  # Loop que percorre todos os recursos do namespace e salva os manifestos
  for resource in "${RESOURCES[@]}"; do
    kubectl get $resource -n $ns -o yaml |
      sed '/^[[:space:]]*uid:/d;
         /^[[:space:]]*resourceVersion:/d;
         /^[[:space:]]*creationTimestamp:/d' >"$ns_backup_dir/$resource.yaml"
  done
  echo "[ * ] $ns namespace backup directory: $BACKUP_DIR/$ns"

  mkdir -p "$ns_backup_dir/pod-logs"

  # Loop que percorre todos os pods e salva os logs
  for pod_name in $(kubectl get pods -n $ns -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}'); do
    echo "    [...] saving logs from $pod_name"
    kubectl logs -n $ns $pod_name >"$ns_backup_dir/pod-logs/$pod_name.log"
  done
  echo ""
done
