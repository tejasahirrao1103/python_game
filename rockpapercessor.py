def rpccode():
    import random
    from re import X

    def rpc():
        while True:
            n=int(input("""
    choose your option 

    1. rock 
    2. paper
    3. sesor
    """))
            x=random.randint(0,3)
            if n==x:
                print("compute and you bot are tie...")
            if n!=x:
                
                if (n==1 and x==3) or (n==2 and x==1) or (n==3 and x==2):
                    print("you win bro")
                else:
                    print("opps.. computer win")

    rpc()
