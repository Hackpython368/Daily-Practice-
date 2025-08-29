quiz_questions = {
        "What does CPU stand for?": ["Central Processing Unit", "Central Process Unit", "Computer Personal Unit", "Control Processing Unit", "Central Processing Unit"],
            
                "Which of the following is an input device?": ["Monitor", "Printer", "Keyboard", "Speaker", "Keyboard"],
                    
                        "What type of memory is RAM?": ["Permanent", "Non-volatile", "Volatile", "External", "Volatile"],
                            
                                "Which company developed the Windows operating system?": ["Apple", "Google", "Microsoft", "IBM", "Microsoft"],
                                    
                                        "What does HTTP stand for?": ["HyperText Transfer Protocol", "HighText Transfer Protocol", "Hyper Transfer Text Protocol", "Hyperlink Transfer Protocol", "HyperText Transfer Protocol"],
                                            
                                                "Which of these is NOT a programming language?": ["Python", "Java", "HTML", "CPU", "CPU"],
                                                    
                                                        "What is the function of an operating system?": ["Process data", "Run antivirus", "Manage computer hardware and software", "Browse the internet", "Manage computer hardware and software"],
                                                            
                                                                "Which of the following is an example of application software?": ["Windows", "Linux", "MS Word", "BIOS", "MS Word"],
                                                                    
                                                                        "What does GUI stand for?": ["Graphical User Interface", "General User Interface", "Graphical Uniform Interface", "Global User Interface", "Graphical User Interface"],
                                                                            
                                                                                "Which storage device has no moving parts?": ["Hard Disk Drive", "Floppy Disk", "CD-ROM", "Solid State Drive", "Solid State Drive"]
                                                                                }

}
score = 0
count = 1
ascii_code = 65
for i in quiz_questions:
    print(f"{count}. {i}")
    for j in quiz_questions[:len(quiz_questions[i])-1]:
        print(f"{chr(ascii_code)}. {j}")
        ascii_code += 1
    ascii_code = 65
    user_input = input()
    if user_input in ["A","B","C","D","a","b","c","d"]:
        if user_input==quiz_questions[i][-1]:
            score += 1

    else:
        print("Wrong Input")
        break

print"You scored : ",score,"/10")