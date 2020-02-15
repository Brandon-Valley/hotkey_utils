import keyboard as k


keep_waiting_for_hotkey_press = True
  
def hotkey_pressed():
    global keep_waiting_for_hotkey_press
    keep_waiting_for_hotkey_press = False
  
  
def wait_for_hotkey_press(hotkey_str):
    k.add_hotkey(hotkey_str, hotkey_pressed)
    while(keep_waiting_for_hotkey_press):
        print('waiting')

        
        
if __name__ == '__main__':
    import time
    wait_for_hotkey_press('a')
    print('done!')


    

    
    
    
    
    
    
    
    
    
