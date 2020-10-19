# Install Prerequisite Software

The first problem every software development team encounters is how to get developers productive quickly and keep them productive by giving them a consistent development environment that is easy to setup and maintain. Some developers might have Mac laptops while others prefer Windows, and still others prefer Linux; but these environments are very different and do not behave the same. 

To solve this problem, will we use VirtualBox and Vagrant to provide an Infrastructure as Code environment on the developers desktop alone with a programmers editor like Vosual Studio Code, and a REST tool like Postman. If you don't have this software installed on your development computer, the first step is down download and install them.

**Note:** _The lab will be using a local Ubuntu 18.04 virtual machine (VM) provisioned and configured by Vagrant._

## Mac Install

[**Homebrew**]((https://brew.sh)) is my preferred method of installing tools on the Mac. First because it is quick and easy, and second because maintaining the latest version is done for you with a simple `brew upgrade` command. If you are tired of downloading software and keeping it up to date, you want to use `brew` instead:

Install **Homebrew** if you don't have it already:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Install **Git**, **VirtualBox**, **Vagrant**, **Visual Studio Code**, and **Postman** using the `brew` command

```sh
brew install git
brew cask install virtualbox
brew cask install vagrant
brew cask install visual-studio-code
brew cask install postman
```

That will install the necessary software for this workshop onto your Mac. If you don't want to use Homebrew, you can follow the Windows installation instructions and install VirtualBox and Vagrant manually. Visual Studio Code and Postman are optional but recommended.

## Windows Install

If you are on Windows you can manually download and install VirtualBox and then Vagrant (in that order)

Link to [VirtualBox](https://www.virtualbox.org/)  

Link to [Vagrant](https://www.vagrantup.com/)  

Link to [Visual Studio Code](https://code.visualstudio.com) (optional but recommended)  

Link to [Postman](https://www.postman.com) (optional but recommended)  

You will also need a [`git`](https://git-scm.com/downloads) client, and `ssh` client.

### Manual Installation

Once you have downloaded all of the software please install VirtualBox and then Vagrant, and then git, Visual Studio Code, and Postman in any order.

[Back](../README.md)
