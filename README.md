# Incident Management with Micro-Services Architecture.
## Reporting Service
<img src="usecase.png"
     alt="Fig. 1: Use Case For The Reporting Service."
     style=" width: 100%; margin: 10px 10px 10px 0;" />
     Fig. 1: Use Case For The Reporting Service.
     <br>

* This service will handle generating bug report for the actors in the system.
* It will take an input of time range to generate the report automatically or manually.
* The report will only be generable by actors with the permission in the system.
* The report will be sent to the actor’s email address.
* The generated report details will be stored to the database.

## ROUGH BREAK DOWN OF ORM IMPLEMENTATION
* Definition
* Report
* Frequency
* Type

#### DEFINITION
<b>Attribute(s) Include:</b><br>id: int<br>frequency: string<br>type_id: int<br>project_uuid: string<br>roles: array<br>user: array<br>created_at: date<br>updated_at: date<br>next_execution_date: date<br><br>
<b>Method(s) Include:</b><br>calculateNextExecDate()<br>
#### REPORT
<b>Attribute(s) Include:</b><br>id: int<br>def_id: int<br>status: string<br>attachment: file<br>created_at: date<br>updated_at: date<br><br>
<b>Method(s) Include:</b><br>generateReport()<br>
#### FREQUENCY
<b>Attribute(s) Include:</b><br>id: int<br>name: string [one-time, daily, weekly & monthly]<br>created_at: date<br>updated_at: date<br><br>
<b>Method(s) Include:</b><br>...<br>
#### TYPE
<b>Attribute(s) Include:</b><br>id: int<br>name: string<br>created_at: date<br>updated_at: date<br><br>
<b>Method(s) Include:</b><br>generateReport()<br>getBugInfo()<br>getIssueInfo()<br>
