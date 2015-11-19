Instances API Reference
=======================

Instances
=========
Represents individual instance on VirtShell.


| Method | HTTP request | Description |
| --- | --- | ---- |
| create | POST | /provisioners/ | Inserts a new provisioner in the system. |
| list | GET | /provisioners | Retrieves the list of provisioners. |
| get | GET | /provisioners/id | Gets one provisioner by ID. |
| delete | DELETE | /provisioners/id | Deletes an existing provisioner. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representation
=======================
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "transactional_log",
  "launch": "1:3",
  "memory": 1024,
  "cpus": 2,
  "hdsize": "2GB",
  "description": "Server transactional only for store logs", 
  "container_resource": "template_name or container image",
  "iso": "ubuntu_server_14.04.2_amd64",
  "host_type": "GeneralPurpose | ComputeOptimized | MemoryOptimized | StorageOptimized",
  "drive": "lxc | virtualbox | vmware | ec2 | kvm | docker",
  "vars" : "https://<host>:<port>/api/virtshell/v1/files/variables/transactional_log_prod.yaml",
  "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
  "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
}
```

###Examples###

`POST /virtshell/api/v1/instances`
--------------------------------------------

Create a new instance.

```sh
curl -sv -X POST \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
        "name": "transactional_log",
        "launch": "1",
        "memory": 1024,
        "cpus": 2,
        "hdsize": "2GB",
        "description": "Server transactional only for store logs", 
        "container_resource": "ubuntu",
        "host_type": "GeneralPurpose",
        "drive": "lxc",
        "vars" : "https://<host>:<port>/api/virtshell/v1/files/variables/transactional_log_prod.yaml",
        "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
        "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
      }' \
   'http://localhost:8080/api/virtshell/v1/instances'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "success" }
```

`GET /virtshell/api/v1/instances/`
----------------------------------------------

Get all instances.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://localhost:8080/api/virtshell/v1/instances'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "instances": [
    {
      "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
      "name": "transactional_log",
      "launch": "1",
      "memory": 1024,
      "cpus": 2,
      "hdsize": "2GB",
      "description": "Server transactional only for store logs", 
      "container_resource": "ubuntu",
      "host_type": "GeneralPurpose",
      "drive": "lxc",
      "vars" : "https://<host>:<port>/api/virtshell/v1/files/variables/transactional_log_prod.yaml",
      "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
      "modified": {"at":"1529207233", "by":"cf744732-8f12-11e5-8994-feff819cdc9f"}
    },
    { 
      "uuid": "cf744476-8f12-11e5-8994-feff819cdc9f",
      "name": "orders_colombia",
      "launch": "1:3",
      "memory": 2024,
      "cpus": 2,
      "hdsize": "4GB",
      "description": "Server transactional dedicated to receive orders", 
      "container_resource": "ubuntu:latest",
      "host_type": "StorageOptimized",
      "drive": "docker",
      "vars" : "https://<host>:<port>/api/virtshell/v1/files/variables/orders_prod.yaml",
      "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
      "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
    }    
  ]
}   
```

`GET /virtshell/api/v1/instances/:id
----------------------------------------------

Get a instance.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://<host>:<port>/api/virtshell/v1/instance/?id=ab8076c0-db91-11e2-82ce-0002a5d5c51b'
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "transactional_log",
  "launch": "1",
  "memory": 1024,
  "cpus": 2,
  "hdsize": "2GB",
  "description": "Server transactional only for store logs", 
  "container_resource": "ubuntu",
  "host_type": "GeneralPurpose",
  "drive": "lxc",
  "vars" : "https://<host>:<port>/api/virtshell/v1/files/variables/transactional_log_prod.yaml",
  "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
  "modified": {"at":"1529207233", "by":"cf744732-8f12-11e5-8994-feff819cdc9f"}
  }
```


`DELETE /virtshell/api/v1/instances/:id`
----------------------------------------------

Delete a existing instance.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://<host>:<port>/api/virtshell/v1/instances?id=ab8076c0-db91-11e2-82ce-0002a5d5c51b'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "success" }
```