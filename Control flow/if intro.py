age = 16
has_ticket = True


if age >= 15 and has_ticket:
    print("You can watch this film")

elif age == 16:
    print("Old enough")
else:
    print("you need to be at least 12 and havew a ticket")
    print("as is this")



print("back to the baseline")
print("This will always run")

film_rating = "U"

if film_rating == "PG":
    print("Suitable for 12 and under but with parental guidance")
else:
    print("Unsuitable")
# U, PG, 12, 12A, 15, 18

# Check the film rating and print a message about who the film is suitable for

#"U" = "Suitable for All"

#"PG" = "Suitable for most but with parental guidance"

#"12" = "12 and over"

#"15" = "15 and over"

#"18" = "18 and over"

age = 12
has_ticket = True

if has_ticket:
    if age>= 15 and has_ticket:
        print("You can see this film.")
    else:
        print("Come back when youre older")
else:
    print("you need a ticket")