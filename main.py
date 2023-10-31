while True:
    print("\033[92mHello!\033[0m") 
    print("Choose an option:")
    print("1 - \033[94mShow next patient\033[0m") 
    print("2 - \033[94mAdd new patient to queue\033[0m") 
    print("3 - \033[94mAttend patient\033[0m") 
    print("4 - \033[94mShow last five attended patients\033[0m")
    print("\033[91m5 - Exit\033[0m")

    option = int(input("Choose an option: "))

    if (option == 5):
        break

