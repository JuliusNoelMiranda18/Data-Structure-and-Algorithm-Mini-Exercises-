def create_waitlist():
    waitlist = []
    return waitlist

def add_to_wailist(waitlist, name):
    waitlist.insert(len(waitlist), name)
    print("Adding " + name + "...")

def remove_from_waitlist(waitlist, name):
    waitlist.remove(name)
    print("Removing " + "'" +  name  + "'" + "...")

def search_waitlist(waitlist, name):
    print("Searching for " + "'" + name + "'" + "...")
    for i in range(len(waitlist)):
        if waitlist[i] == (name):
            print("Found " + "'" + name + "' " + "at index " + str(i) + "\n")
            return
    print("Not found" + "\n")

def traverse_waitlist(waitlist):
    print("[", end="")
    for name in waitlist:
        if name == waitlist[len(waitlist) - 1]: 
            print("'" + name + "'", end="")
        else:
            print("'" + name + "', ", end="")
    print("]")

def create_chart(rows, cols):
    chart = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(None)
        chart.append(row)
    return chart

def assign_seat(chart, row, col, name):
    if chart[row][col] is None:
        chart[row][col] = name
        print("Row " + str(row) + ", Col " + str(col) + " -> " + name)
    else:
        print("Occupied")

def clear_seat(chart, row, col):
    print("Clearing seat " + "(" + str(row) + "," + str(col) + ")...")
    chart[row][col] = None

def traverse_chart(chart):
    print("Update Seating Chart: ")
    for i in range(len(chart)):
        print("Row " + str(i) + ": "  + str(chart[i]))

print("=== CINEMA WAITLIST ===")
cinema_waitlist = create_waitlist()
print("Initial waitlist: ", end="")
traverse_waitlist(cinema_waitlist)

add_to_wailist(cinema_waitlist, "Ana")
add_to_wailist(cinema_waitlist, "Ben")
add_to_wailist(cinema_waitlist, "Cara")
add_to_wailist(cinema_waitlist, "Dan")
add_to_wailist(cinema_waitlist, "Eli")
print("Current waitlist: ", end="")
traverse_waitlist(cinema_waitlist)
print(" ")

remove_from_waitlist(cinema_waitlist, "Cara")
print("Waitlist after removal: ", end="")
traverse_waitlist(cinema_waitlist)
print(" ")

search_waitlist(cinema_waitlist, "Ben")        

print("Final Waitlist: ", end="")
traverse_waitlist(cinema_waitlist)

print("=== SEATING CHART ===")
seating_chart = create_chart(3,4)
print("Assigning seats...")
assign_seat(seating_chart, 0, 1, "Ana")
assign_seat(seating_chart, 1, 2, "Ben")
assign_seat(seating_chart, 2, 3, "Dan")
print("")

clear_seat(seating_chart, 1, 2)
traverse_chart(seating_chart)



    



