# Working with Vagrant and VirtualBox

This workshop is conducted inside of an Ubuntu virtual machine (VM) that is configured and managed by Vagrant so that every participan gets the exact same development environment. This is know was **Infrastructure as Code** where we codify the instructions to create computing environments that are exact replicas of each other.

## Bring up the Ubuntu Linux Virtual Machine

Once you have installed the [prerequisite software](00-install-prereqs.md), you are ready to `clone` the project to your development folder and create your Vagrant VM. Open a terminal/shell window and change to a folder on your computer that you want to keep the source code for this workshop.

```sh
  git clone https://github.com/rofrano/devops-workshop.git
  cd devops-workshop
  vagrant up
```

This will bring up the VM and install a Python 3 development environment with `microk8s` (a small Kubernetes distribution) and the Kubernetes CLI (`kubectl`) for deploying to Kubernetes.

## Using the VM

Vagrant sets up private `ssh` so that you don't need a key. This VM should be treated just like a remote server in the cloud. To get into it use:

```sh
  vagrant ssh
```

You should now be inside the VM and ready to follow alone with the workshop.

## Exiting the VM and shutting it down

Just like a remote server, you logout of the VM using the `exit` command. You can also shutdown the virtual machine using the `vagrant halt` command:

```sh
  exit
  vagrant halt
```

This will shutdown the VM. When are are ready to use it again, just `cd` into the `devops-workshop` folder and use `vagrant up` to bring it back up.

## Removing the Virtual Machine

You can remove the vagrant VM to free up space on your computer or to recreate it again because something has gone horribly wrong. If we keep all of our work under the `/vagrant` folder, it will be safely stored on our computer and the VM can be destroyed and recreated at any time with:

```sh
  vagrant destroy
```

This will delete the virtual machine from your computer.

## Global Status

As you use Vagrant you will want to know if you left any virtual machines running. This can be easily seen using the `vagrant global-status` command:

```sh
  vagrant global-status
```

The results on my Mac were:

```sh
  $ vagrant global-status
  id       name    provider   state    directory
  ---------------------------------------------------------------------------
  33160a7  default virtualbox poweroff /Users/rofrano/GitHub/devops-workshop

  The above shows information about all known Vagrant environments
  on this machine. This data is cached and may not be completely
  up-to-date (use "vagrant global-status --prune" to prune invalid
  entries). To interact with any of the machines, you can go to that
  directory and run Vagrant, or you can use the ID directly with
  Vagrant commands from any directory. For example:
  "vagrant destroy 1a2b3c4d"
```

This shows that I have a vagrant VM defined under `/Users/rofrano/GitHub/devops-workshop` and that it is currently in the `poweroff` state. _Hint: If your laptop batter is excessively draining and you don't know why, it's always a good idea to check and see if you left any virtual machines running in the background!_
