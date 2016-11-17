# JIRA Acess Log Analyser
This script can be used to analyse the jira access logs assuming they
were saved with the default log settings from <install>/conf/server.xml:
```xml
<Valve className="org.apache.catalina.valves.AccessLogValve"
                  pattern="%a %{jira.request.id}r %{jira.request.username}r %t &quot;%m %U%q %H&quot; %s %b %D &quot;%{Referer}i&quot; &quo
t;%{User-Agent}i&quot; &quot;%{jira.request.assession.id}r&quot;”/>
```
# Usage
This script only works with python 2!
Access Logs must be in the same dir as the files. Filenames must start with `access_log`.

Run `python make.py` to generate the html reports in a timestamped directory.