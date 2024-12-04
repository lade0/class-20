#function to check palindrone
def pal(r):
    st=0
    end=len(r)-1
    while st<end:
        if r[st]!=r[end]:
            return False
        st=st+1
        end=end-1
    return True
r=(50,40,50,50,50,50,40,50)
if pal(r):
    print("the tuple is a palindrone")
else:
    print("the tuple is not a palindrone")
