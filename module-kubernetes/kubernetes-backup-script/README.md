# Exercícios 1

---
**Requisitos**

- Faça um script que:
    1. percorra todos os namespaces;
    1. liste todos os recursos instalados;
    1. realize uma cópia de segurança de cada manifesto;
- Dicas:
    1. faça uma lista de todos os recursos que você deseja copiar e
    para cada namespace percorra essa lista.
    1. use o comando kubectl get -o yaml que é uma das formas mais
    simples de copiar o manifesto.
    1. pense em como vai ser a dinâmica da execução e estabeleça
    uma estrutura de pastas e nomes de arquivos antes de começar.
- Bônus1: Fazer também o script para aplicar todos os manifestos.
- Bônus2: Copiar também os logs dos pods.
- Bônus3: Colocar uma lista de namespaces que não precisam de
backup.
---

### Descrição da Abordagem:

Neste exercício foram criados dois scrips para backup: `backup-all.sh` e `restore.sh`, responsaveis por realizar o backup de determinados namespaces do seu cluster kubernetes no formato .yaml e realizar o restore através dos manifestos salvos, respectivamente.

### Realizando backup:

Para fazer o backup dos namespaces do seu cluster kubernetes, basta executar em um terminal:

```bash
bash backup-all.sh
```

### Realizando restore:

Para fazer o restore dos namespaces em seu cluster kubernetes, basta executar em um terminal:

```bash
bash restore.sh
```
