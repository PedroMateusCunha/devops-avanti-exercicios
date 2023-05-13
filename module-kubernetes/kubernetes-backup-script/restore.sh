#!/bin/bash

BACKUP_DIR=/tmp/k8s-backup
RESOURCES="namespaces configmaps secrets deployments services"

# Loop em todos os namespaces
for ns_backup_dir in $(find "$BACKUP_DIR" -maxdepth 1 -type d | tail -n +2); do
  ns=$(basename "$ns_backup_dir")
  # Verifica se a pasta de backup para o namespace existe
  if [ ! -d "$ns_backup_dir" ]; then
    echo "[ ! ] No backup found for namespace $ns_backup_dir"
    continue
  fi
  echo ""
  echo "NAMESPACE: $ns"
  echo "======================================================="
  echo "[ * ] Applying backup to the namespace $ns"

  # Loop em todos os recursos
  for resource in ${RESOURCES}; do
    # Aplica o arquivo YAML do recurso
    yaml_file="$BACKUP_DIR/$ns/$resource.yaml"
    if [ -f "$yaml_file" ]; then
      echo "  [ * ] Applying $ns $yaml_file"
      kubectl apply -f "$yaml_file" -n $ns
      echo ""
    fi
  done

  # for log_file in "$ns_backup_dir/pod-logs"/*.log; do
  #   # TO DO 
  #   # pod_name=$(basename "$log_file" .log)
  #   # echo "    [...] Restoring logs for pod $pod_name"
  #   # kubectl logs -n $ns $pod_name <$log_file >> logs.logs
  # done
done
