import os,time

cal1=(75*5.26)
cal2=(125*7.2)
cal3=(100*7.59)
cal4=(100*8.02)
cal5=(200*12.67)

use = float(input("\nTotal Unit (KWH/Unit): "))
load = float(input("Demand Load (KW): "))

def extra_cal(load,use,main_cal):
    demand_charge=42
    extra_cal_1=(load*demand_charge)
    vat_count = ((main_cal+extra_cal_1)*(5/100))
    total_bill=(main_cal+extra_cal_1+vat_count)
    show_total = round(total_bill, 2)
    vat_ammount_show = round(vat_count, 2)
    
    print(f"Vat Ammount : {vat_ammount_show}Tk\nDemand Charge: {extra_cal_1}Tk")
    print("\n---------------------------------")
    print(f"Total Bill: {show_total}Tk")
    print("---------------------------------\n")

def banner():
    time.sleep(3)
    print("\n***********************************************")
    print("    Electricity Bill Calculate -- TR FAHIM")
    print("***********************************************\n")
    
if use <= 75:
    main_cal = (use*5.26)
    os.system("cls")
    banner()
    print(f"\nElectricity Bill: {round(main_cal, 2)}Tk")
    extra_cal(load,use,main_cal)
      
elif use <= 200:
    t_cal=use-75
    f_cal = t_cal*7.2
    main_cal = (cal1+f_cal)
    os.system("cls")
    banner()
    print(f"\nElectricity Bill: {round(main_cal, 2)}tk")
    extra_cal(load,use,main_cal)
    
elif use <= 300:
    t_cal=use-200
    f_cal = t_cal*7.59
    main_cal = (cal1+cal2+f_cal)
    os.system("cls")
    banner()
    print(f"\nElectricity Bill: {round(main_cal, 2)}tk")
    extra_cal(load,use,main_cal)
    
elif use <= 400:
    t_cal=use-300
    f_cal = t_cal*8.02
    main_cal = (cal1+cal2+cal3+f_cal)
    os.system("cls")
    banner()
    print(f"\nElectricity Bill: {round(main_cal, 2)}tk")
    extra_cal(load,use,main_cal)
    
elif use <= 600:
    t_cal=use-400
    f_cal = t_cal*12.67
    main_cal = (cal1+cal2+cal3+cal4+f_cal)
    os.system("cls")
    banner()
    print(f"Electricity Bill: {round(main_cal, 2)}tk")
    extra_cal(load,use,main_cal)
    
elif use > 600:
    t_cal=use-600
    f_cal = t_cal*14.61
    main_cal = (cal1+cal2+cal3+cal4+cal5+f_cal)
    os.system("cls")
    banner()
    print(f"Electricity Bill: {round(main_cal, 2)}tk")
    extra_cal(load,use,main_cal)
    
else:
    print("Wrong Input !!")    

