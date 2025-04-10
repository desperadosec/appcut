# AppCut
AppCut is a supplemental tool to extend and extract the functionality of IDA Pro's AppCall function.

The IDA API AppCall function allows an analyst to call an unexported function within a binary. For instance, if a piece of malware has a Domain Generation Algorithm (DGA) or custom encoder, AppCall can be used to invoke it with arbitrary parameters and use the function to obtain results.

But what if you want to extend this, or use a function without having to start IDA? I designed AppCut to export the function to a binary blob, and allow malware analysts to wrap the function with CTypes and invoke it via Python. This way, a function can be incorporated into a larger framework, automated malware analysis script, and so on.
