# ERPNext Autocount Integration


## Autocount integration for Frappe
Autocount ERPNext custom app is built based on [Autocount Accounting 2.0](https://www.autocountsoft.com/pro-accounting2.html) software. It is built to integrate with ERPNext, act as a connector that allows bidirectional data transfer between Autocount software and ERPNext. With Autocount ERPNext custom app, only one copy of Autocount software is required to install on the main computer, other computers in the same network can read or write data through ERPNext. More information can be found in the [Wiki section](https://github.com/msf4-0/ERPNext-Autocount-Integration/wiki).

## Installation

### Pre-requisites
1. Autocount Accounting 2.0

- Refers to: https://www.autocountsoft.com/pro-accounting2.html

2. MyAutocount API server and service.

- Download and installation guide is available at: https://github.com/msf4-0/MyAutocount

3. Installed ERPNext which runs on localhost. 

- Installation guide refers to: https://github.com/msf4-0/IRPS-Autocount-Integration

## Setup
By default, the IP address is set to docker localhost with port of 8888 (http://host.docker.internal:8888). If the app is not running on main computer which installs Autocount software, users must configure the settings before using.

1. 


## Important Note
Autocount ERPNext custom app may not validate data when being exported to Autocount software. The user must have basic knowledge of Autocount to avoid any error. 

## Author
1. [Timothy Wong](https://github.com/Tim1702)

## License
This software is licensed under the [GNU GPLv3 LICENSE](/LICENSE) © [Selangor Human Resource Development Centre](http://www.shrdc.org.my/). 2022.  All Rights Reserved.
