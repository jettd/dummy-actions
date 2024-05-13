# inf loop testing.
def main():
    i = 0; 
    while True:  
        i += 2 
    return "inf_loop_ended_somehow" #should never end. 

if __name__ == "__main__":
    result = main()
    print(result)
