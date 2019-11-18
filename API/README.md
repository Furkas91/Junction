# Cloud Infrastructure

Your team has been provided a vm running on Azure. It runs Ubuntu 18.04.

## VM details

* Flavour : Standard_D2_v2
* IP address : 192.168.1.9
* Username : torvalds
* jumphost : jumphost.citysimulation.eu
* jumphost username : torvalds
* SSH port : 22

## Provided credentials

In this folder you will get three files :

* id_rsa : private key to access your vm
* id_rsa.pub : public key associated to the private key
* https_key : your key to access the admin interface of your server

## Accessing your vm

You first need to have an ssh agent running and add the private key:

```sh
eval $(ssh-agent) && ssh-add ./id_rsa
```

Then you can access the vm by ssh through the jumphost :

```sh
ssh -A \
  -o ProxyCommand="ssh -A -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -W %h:%p torvalds@jumphost.citysimulation.eu" \
  torvalds@192.168.1.9
```

Alternatively you can create an ssh config:

```
Host 192.168.1.9
  User torvalds
  ProxyCommand ssh  -W %h:%p citysimulation_jumphost
  ForwardAgent yes
Host citysimulation_jumphost
  User torvalds
  ForwardAgent yes
  Hostname jumphost.citysimulation.eu
```

and then ssh normally :

```sh
ssh 192.168.1.9
```
