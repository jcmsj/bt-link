# A script that updates link keys given a registry file

## windows side:
1. Download and Extract [PS Tools](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec)
2.  Cd in the extracted folder
3. Run:
```ps
.\PsExec64.exe -s -i regedit /e C:\BTKeys.reg HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\BTHPORT\Parameters\Keys
```
4. copy BTKeys.reg to a drive that your linux has access to
5. boot to linux

## Linux side:
1. assuming you cd'd to the reg file's location, run 
```bash
python extract_pairs.py ./BTKeys.reg
```
2. see [todos](todo.md)    

