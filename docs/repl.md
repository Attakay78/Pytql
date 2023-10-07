## ReplType
!!! tip ""
    <i style="font-size:18px;"> <span style="color:blue-grey"> class </span> <span style="color:teal">pytql.repl.ReplType</span>
    </i>

<br>

Class listing of cli repl types.

> default_repl

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default repl to run Pytql client. Non-interactive.

<br>


> interactive_repl

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Interactive repl to run PyTQL client. Interactive but no autocomplete.


<br>


> ipython_repl

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Interactive repl to run Pytql client. Supports autocomplete and autosuggestions.

<br>

<center>
Image of code sample and it's output run from the **ipython_repl** cli client.<br><br>
<img src="../repl.png" alt="Student Table" width="600" />
</center>

<br>

!!! tip ""
    <i style="font-size:18px;"> <span style="color:blue-grey"> function </span> <span style="color:teal">pytql.repl.start_client</span>
    <span style="color:blue-grey">(module_name, repl_type: ~pytql.repl.ReplType = <function default_repl>)</span>
    </i>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Function to start the Pytql client repl. <br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Args**: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; module_name : Name of the module PyTQL is being run from. Always pass 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`__name__` as the value.<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; repl_type : Repl type to use. Defaults to ReplType.default_repl.

<br>
