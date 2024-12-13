# Minio deployment

```
chmod +x minio-deploy.sh
./minio-deploy.sh
```

# MariaDB deployment
1. edit file `dependencies/mariadb/mariadb-np.yml` line 29 and line 36

    ```
    kubernetes.io/metadata.name: mas-<yourinstance>-aibroker
    ```

    for example: `mas-apmdevops-aibroker`
    
    **NOTICE:**
    _Please use the same instance name from maximo core_
2. Run following
    ```
    chmod +x mariadb-deploy.sh
    ./mariadb-deploy.sh
    ```