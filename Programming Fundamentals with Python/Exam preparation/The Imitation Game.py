encrypted_message = input()
instructions = input()

while instructions != "Decode":
    instructions = instructions.split("|")
    command = instructions[0]
    if command == "ChangeAll":
        replaced_letter = instructions[1]
        new_letter = instructions[2]
        temp = encrypted_message.replace(replaced_letter, new_letter)
        encrypted_message = temp
    elif command == "Insert":
        insert_index = int(instructions[1])
        insert_letter = instructions[2]
        encrypted_message = encrypted_message[:insert_index] + insert_letter + encrypted_message[insert_index:]
    elif command == "Move":
        move_quantity = int(instructions[1])
        temp = encrypted_message[:move_quantity]
        encrypted_message = encrypted_message[move_quantity:] + temp

    instructions = input()

print(f"The decrypted message is: {encrypted_message}")