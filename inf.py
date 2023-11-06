# Test Script 1
def main():
    i = 0; 
    while true:  
        i += 1 
    return "inf_loop_ended_somehow" #should never end. 

if __name__ == "__main__":
    result = main()
    print(result)
