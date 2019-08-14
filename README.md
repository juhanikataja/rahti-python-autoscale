# Automatically scaling a python web application

This demo illustrates Kubernetes' automatic scaler which increases or decreases
the number of pods depending on their cpu usage.

## How to deploy

Authorize the CLI session.

### From local sources

Use the `oc new-app`:
```bash
oc new-app . --name=python-load --labels='app=python-load' -e APP_FILE=src/app.py
```

The build will fail because the sources are not automatically uploaded.
Lets upload them with `oc start-build`:

```bash
oc start-build python-load --from-dir=. -F
```

### From remote git repository

Use the `oc new-app`:
```bash
oc new-app https://github.com/juhanikataja/rahti-python-autoscale --name=python-load --labels='app=python-load' -e APP_FILE=src/app.py
```


## Expose to internet and modify the DeploymentConfig

Lets expose the service (choose proper hostname):

```bash
oc expose service python-load --hostname='jkataja-python-load.rahtiapp.fi'
```

Modify CPU request with patch command:

```bash
oc patch dc python-load -p 'spec: {template: {spec: {containers: [{name: python-load, resources: {requests: {cpu: 1}}}]}}}'
```

## Autoscale

Add autoscaler

```bash
oc autoscale dc python-load --min=1 --max=3 --cpu-percent=80
```

The `cpu-percent` in the autoscaler is the percentage from the cpu resource
request. This is why we issued the monstrous patch command to modify the
resource requests above.
