
TASK [ibm.mas_devops.odh : determine-storage-classes : Lookup storage classes] *****************************************************************************
An exception occurred during task execution. To see the full traceback, use -vvv. The error was:     raise ApiException(http_resp=r)
fatal: [localhost]: FAILED! => changed=false 
  module_stderr: |-
    Traceback (most recent call last):
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/dynamic/client.py", line 55, in inner
        resp = func(self, *args, **kwargs)
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/dynamic/client.py", line 270, in request
        api_response = self.client.call_api(
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/client/api_client.py", line 348, in call_api
        return self.__call_api(resource_path, method,
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/client/api_client.py", line 180, in __call_api
        response_data = self.request(
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/client/api_client.py", line 373, in request
        return self.rest_client.GET(url,
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/client/rest.py", line 244, in GET
        return self.request("GET", url,
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/client/rest.py", line 238, in request
        raise ApiException(http_resp=r)
    kubernetes.client.exceptions.ApiException: (401)
    Reason: Unauthorized
    HTTP response headers: HTTPHeaderDict({'Audit-Id': '4071ec90-b4ef-408b-b191-461c32f552da', 'Cache-Control': 'no-cache, private', 'Content-Type': 'application/json', 'Strict-Transport-Security': 'max-age=31536000', 'Date': 'Thu, 05 Sep 2024 10:46:35 GMT', 'Content-Length': '129'})
    HTTP response body: b'{"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}\n'
  
  
    During handling of the above exception, another exception occurred:
  
    Traceback (most recent call last):
      File "/root/.ansible/tmp/ansible-tmp-1725533193.5466933-1311-35606284652703/AnsiballZ_k8s_info.py", line 107, in <module>
        _ansiballz_main()
      File "/root/.ansible/tmp/ansible-tmp-1725533193.5466933-1311-35606284652703/AnsiballZ_k8s_info.py", line 99, in _ansiballz_main
        invoke_module(zipped_mod, temp_path, ANSIBALLZ_PARAMS)
      File "/root/.ansible/tmp/ansible-tmp-1725533193.5466933-1311-35606284652703/AnsiballZ_k8s_info.py", line 47, in invoke_module
        runpy.run_module(mod_name='ansible_collections.kubernetes.core.plugins.modules.k8s_info', init_globals=dict(_module_fqn='ansible_collections.kubernetes.core.plugins.modules.k8s_info', _modlib_path=modlib_path),
      File "/usr/lib64/python3.9/runpy.py", line 225, in run_module
        return _run_module_code(code, init_globals, run_name, mod_spec)
      File "/usr/lib64/python3.9/runpy.py", line 97, in _run_module_code
        _run_code(code, mod_globals, init_globals,
      File "/usr/lib64/python3.9/runpy.py", line 87, in _run_code
        exec(code, run_globals)
      File "/tmp/ansible_kubernetes.core.k8s_info_payload_5dq8mw6g/ansible_kubernetes.core.k8s_info_payload.zip/ansible_collections/kubernetes/core/plugins/modules/k8s_info.py", line 202, in <module>
      File "/tmp/ansible_kubernetes.core.k8s_info_payload_5dq8mw6g/ansible_kubernetes.core.k8s_info_payload.zip/ansible_collections/kubernetes/core/plugins/modules/k8s_info.py", line 198, in main
      File "/tmp/ansible_kubernetes.core.k8s_info_payload_5dq8mw6g/ansible_kubernetes.core.k8s_info_payload.zip/ansible_collections/kubernetes/core/plugins/modules/k8s_info.py", line 156, in execute_module
      File "/tmp/ansible_kubernetes.core.k8s_info_payload_5dq8mw6g/ansible_kubernetes.core.k8s_info_payload.zip/ansible_collections/kubernetes/core/plugins/module_utils/common.py", line 262, in kubernetes_facts
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/dynamic/client.py", line 112, in get
        return self.request('get', path, **kwargs)
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/dynamic/client.py", line 57, in inner
        raise api_exception(e)
    kubernetes.dynamic.exceptions.UnauthorizedError: 401
    Reason: Unauthorized
    HTTP response headers: HTTPHeaderDict({'Audit-Id': '4071ec90-b4ef-408b-b191-461c32f552da', 'Cache-Control': 'no-cache, private', 'Content-Type': 'application/json', 'Strict-Transport-Security': 'max-age=31536000', 'Date': 'Thu, 05 Sep 2024 10:46:35 GMT', 'Content-Length': '129'})
    HTTP response body: b'{"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}\n'
    Original traceback:
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/dynamic/client.py", line 55, in inner
        resp = func(self, *args, **kwargs)
  
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/dynamic/client.py", line 270, in request
        api_response = self.client.call_api(
  
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/client/api_client.py", line 348, in call_api
        return self.__call_api(resource_path, method,
  
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/client/api_client.py", line 180, in __call_api
        response_data = self.request(
  
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/client/api_client.py", line 373, in request
        return self.rest_client.GET(url,
  
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/client/rest.py", line 244, in GET
        return self.request("GET", url,
  
      File "/opt/app-root/lib64/python3.9/site-packages/kubernetes/client/rest.py", line 238, in request
        raise ApiException(http_resp=r)
  module_stdout: ''
  msg: |-
    MODULE FAILURE
    See stdout/stderr for the exact error
  rc: 1
