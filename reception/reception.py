def registration_checker(person_name=input("Enter a single name: ")):
    
    vip_list_text_file=open("guest lists/vip_list.txt")
    vip_file_content=vip_list_text_file.read()
    vip_guest_names_list=[]
    vip_guest_names_list=vip_file_content.split("\n")
    for number in range(0,len(vip_guest_names_list)):
        if person_name.lower() in vip_guest_names_list[number].lower():
            return (vip_guest_names_list[number]+", VIP")
        else:
            VIP_status="false"
    ordinary_list_text_file=open("guest lists/ordinary_list.txt")
    ordinary_file_content=ordinary_list_text_file.read()
    ordinary_guest_names_list=[]
    ordinary_guest_names_list=ordinary_file_content.split("\n")
    for index in range(0,len(ordinary_guest_names_list)):
        if person_name.lower() in ordinary_guest_names_list[index].lower():
            return (ordinary_guest_names_list[index]+", Ordinary")
        else:
            ordinary_status="false"
    if  VIP_status=="false" and  ordinary_status=="false":
        return("Not registered")        
print(registration_checker())  
            
    
  
