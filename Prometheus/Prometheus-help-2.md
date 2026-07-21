
#############   chatgpt.com ##################################

    1- what is Prometheus ?
    2- how install Prometheus on windows ?

        cd C:\nssm\win64



####  Monitoring Windows servers using Prometheus — wmi_exporter

    https://rakeshjain-devops.medium.com/monitoring-windows-servers-using-prometheus-wmi-exporter-eb082fcbaffb
    https://rm-rf.medium.com/install-windows-exporter-grafana-monitoring-for-windows-server-c116dad7142e
    https://www.devopsschool.com/blog/how-to-install-windows-exporter-for-prometheus/

    Step 1-  First, we will download install Node Exporter on all machines :
             download from browser
             https://github.com/prometheus-community/windows_exporter/releases

             windows_exporter-0.30.4-amd64.msi

             - Note : make sure 'Enhanced Security Configuration' off
             - Install above msi
             - The port to bind to. Defaults to 9182.
             - validate – http://ip-address:9182/metrics
                    http://192.168.5.201:9182/metrics

    Step 2-    install Prometheus on Windows (See Above)             




### windows_exporter Vs wmi_exporter
    -windows_exporter includes all the functionality of wmi_exporter but comes with:
        -Better codebase maintenance
        -Improved performance and stability
        -Expanded metrics coverage
        -Enhanced support for modern Windows versions
    Note:
        - windows_exporter is now the official Prometheus exporter for Windows metrics.
        - wmi_exporter is no longer actively maintained, and new features or updates will not be provided.







https://www.youtube.com/watch?v=eHZdfAsMLSw
https://www.youtube.com/watch?v=evVTjiz3bHM&list=PLVCgi5HZ0-Ytx5J5fp7A4HG5HreQ-7ZMg
https://www.youtube.com/watch?v=QoDqxm7ybLc

https://www.youtube.com/watch?v=h4Sl21AKiDg&list=PLy7NrYWoggjxCF3av5JKwyG7FFF9eLeL4&index=1


### System Monitoring using Prometheus & Grafana

    https://www.youtube.com/watch?v=fTQpEoldU3k

#### Prometheus and Grafana Tutorial    
    https://www.youtube.com/watch?v=DuYnPOq4D6w&list=PLdsu0umqbb8NxUs8r8BIUe9-PhcoZyojA&index=1



 https://www.youtube.com/watch?v=QwGm5m4AxNA   



### Windows Exporter for prometheus (to check the server health)
    - download and install 'Windows Exporter' and configure with grafana

         

    - create Grafana Dashboard
         https://www.youtube.com/watch?v=rt55FcSyl4o&t=180s
         https://grafana.com/grafana/dashboards/15620-windows-node-exporter/
