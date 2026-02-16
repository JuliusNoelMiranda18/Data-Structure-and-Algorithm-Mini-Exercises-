# Course Prerequisites Tree (forest by year)

class Node:
    """A node in a general (k-ary) tree. children is a simple Python list."""
    def __init__(self, value):
        self.value = value
        self.children = []  # list of Node objects
    
    def add_child(self, child):
        """Attach child (Node) as the next child of this node."""
        if not isinstance(child, Node):
            raise TypeError("child must be a Node")
        self.children.append(child)
    
    def __repr__(self):
        return f"Node({self.value!r})"


class Forest:
    """A simple container for multiple tree roots (useful to show forests)."""
    def __init__(self):
        self.roots = []  # list of Node roots
    
    def add_tree(self, root):
        if not isinstance(root, Node):
            raise TypeError("root must be a Node")
        self.roots.append(root)
    
    def print_forest(self):
        for i, r in enumerate(self.roots, 1):
            print(f"Year {i} - {r.value}:")
            print_tree(r)
            print("-" * 20)


# ---------- Helper functions for printing and traversal ----------

def print_tree(node, indent=0):
    """Print the tree with indentation (parent above children)."""
    if node is None:
        return
    print("  " * indent + str(node.value))
    for child in node.children:
        print_tree(child, indent + 1)


def preorder(node, visit):
    """Preorder traversal: visit node, then children left-to-right."""
    if node is None:
        return
    visit(node)
    for child in node.children:
        preorder(child, visit)


def search(node, name):
    """Find and return the node whose value matches name (exact match)."""
    if node is None:
        return None
    if node.value == name:
        return node
    for child in node.children:
        found = search(child, name)
        if found:
            return found
    return None


def search_forest(forest, name):
    """Search all roots in a forest and return the first matching node."""
    for root in forest.roots:
        found = search(root, name)
        if found:
            return found
    return None


# ---------- Build a sample program as a forest (1st-4th year) ----------

def build_sample_forest():
    f = Forest()
    
    # Year roots
    y1 = Node("1st Year")
    y2 = Node("2nd Year")
    y3 = Node("3rd Year")
    y4 = Node("4th Year")
    
    # add roots to forest
    f.add_tree(y1)
    f.add_tree(y2)
    f.add_tree(y3)
    f.add_tree(y4)
    
    # ===== 1st Year - 1st Semester =====
    ge1 = Node("GE 1")
    ge2 = Node("GE 2")
    ge3 = Node("GE 3")
    math83 = Node("Math 83 (Essentials of Analysis I)")
    math101 = Node("Math 101 (Elementary Statistics)")
    cmsc11 = Node("CMSC 11 (Introduction to Computer Science)")
    pe1 = Node("PE (1st Sem)")
    nstp1 = Node("NSTP (1st Sem)")
    
    y1.add_child(ge1)
    y1.add_child(ge2)
    y1.add_child(ge3)
    y1.add_child(math83)
    y1.add_child(math101)
    y1.add_child(cmsc11)
    y1.add_child(pe1)
    y1.add_child(nstp1)
    
    # Add prerequisites (children) for 1st semester courses
    math83.add_child(Node("HS Algebra & Trigonometry"))
    math101.add_child(Node("HS Algebra & Trigonometry"))
    
    # ===== 1st Year - 2nd Semester =====
    ge4 = Node("GE 4")
    math84 = Node("Math 84 (Essentials of Analysis II)")
    physics71 = Node("Physics 71 (Elementary Physics I)")
    cmsc21 = Node("CMSC 21 (Fundamentals of Programming)")
    cmsc55 = Node("CMSC 55 (Discrete Mathematical Structures in Computer Science)")
    pe2 = Node("PE (2nd Sem)")
    nstp2 = Node("NSTP (2nd Sem)")
    
    y1.add_child(ge4)
    y1.add_child(math84)
    y1.add_child(physics71)
    y1.add_child(cmsc21)
    y1.add_child(cmsc55)
    y1.add_child(pe2)
    y1.add_child(nstp2)
    
    # Add prerequisites for 2nd semester courses
    math84.add_child(Node("Math 83"))
    physics71.add_child(Node("Math 83"))
    cmsc21.add_child(Node("CMSC 11"))
    cmsc55.add_child(Node("CMSC 11"))
    
    # ===== 2nd Year - 1st Semester =====
    ge5 = Node("GE 5")
    math85 = Node("Math 85 (Essentials of Analysis III)")
    chem32 = Node("Chem 32 (Chemistry of Biomolecules)")
    cmsc22 = Node("CMSC 22 (Object-Oriented Programming Paradigms)")
    cmsc123 = Node("CMSC 123 (Data Structures)")
    cmsc130 = Node("CMSC 130 (Logic Design & Digital Computer Circuits)")
    cmsc171 = Node("CMSC 171 (Ethical & Social Issues in Computer Science)")
    pe3 = Node("PE (3rd Sem)")
    
    y2.add_child(ge5)
    y2.add_child(math85)
    y2.add_child(chem32)
    y2.add_child(cmsc22)
    y2.add_child(cmsc123)
    y2.add_child(cmsc130)
    y2.add_child(cmsc171)
    y2.add_child(pe3)
    
    # Add prerequisites for 2nd year 1st semester courses
    math85.add_child(Node("Math 84"))
    cmsc22.add_child(Node("CMSC 21"))
    cmsc123.add_child(Node("CMSC 21"))
    cmsc123.add_child(Node("CMSC 55"))
    cmsc130.add_child(Node("CMSC 55"))
    
    # ===== 2nd Year - 2nd Semester =====
    ge6 = Node("GE 6")
    stat121 = Node("Stat 121 (Applied Probability Models)")
    cmsc121 = Node("CMSC 121 (Web Programming)")
    cmsc124 = Node("CMSC 124 (Design & Implementation of Programming Languages)")
    cmsc127 = Node("CMSC 127 (Database Systems)")
    cmsc135 = Node("CMSC 135 (Computer Organization & Architecture)")
    pe4 = Node("PE (4th Sem)")
    
    y2.add_child(ge6)
    y2.add_child(stat121)
    y2.add_child(cmsc121)
    y2.add_child(cmsc124)
    y2.add_child(cmsc127)
    y2.add_child(cmsc135)
    y2.add_child(pe4)
    
    # Add prerequisites for 2nd year 2nd semester courses
    stat121.add_child(Node("Math 101"))
    cmsc121.add_child(Node("CMSC 22"))
    cmsc124.add_child(Node("CMSC 123"))
    cmsc127.add_child(Node("CMSC 123"))
    cmsc135.add_child(Node("CMSC 21"))
    cmsc135.add_child(Node("CMSC 130"))
    
    # ===== 3rd Year - 1st Semester =====
    stat122 = Node("Stat 122 (Applied Bayesian Inferential Models)")
    math120 = Node("Math 120 (Linear Algebra)")
    cmsc125 = Node("CMSC 125 (Operating Systems)")
    cmsc122 = Node("CMSC 122 (Human Computer Interaction)")
    cmsc1281 = Node("CMSC 128.1 (Software Engineering I)")
    cmsc176 = Node("CMSC 176 (Fundamentals of Data Science)")
    
    y3.add_child(stat122)
    y3.add_child(math120)
    y3.add_child(cmsc125)
    y3.add_child(cmsc122)
    y3.add_child(cmsc1281)
    y3.add_child(cmsc176)
    
    # Add prerequisites for 3rd year 1st semester courses
    stat122.add_child(Node("Stat 121"))
    math120.add_child(Node("Math 85"))
    cmsc125.add_child(Node("CMSC 123"))
    cmsc122.add_child(Node("CMSC 121"))
    cmsc1281.add_child(Node("CMSC 121"))
    cmsc1281.add_child(Node("CMSC 127"))
    cmsc176.add_child(Node("CMSC 127"))
    cmsc176.add_child(Node("Stat 121"))
    
    # Major Course 1 options
    major1_stat = Node("Major Course 1: Stat 130 (Nonparametric Statistical Methods)")
    major1_hi = Node("Major Course 1: HI 191 (Fundamentals of Health Informatics)")
    
    y3.add_child(major1_stat)
    y3.add_child(major1_hi)
    
    major1_stat.add_child(Node("Math 101"))
    
    # ===== 3rd Year - 2nd Semester =====
    math1211 = Node("Math 121.1 (Elementary Differential Equations I)")
    cmsc1282 = Node("CMSC 128.2 (Software Engineering II)")
    cmsc138 = Node("CMSC 138 (Computer Networks)")
    cmsc161 = Node("CMSC 161 (Interactive Computer Graphics)")
    cmsc177 = Node("CMSC 177 (Model Building and Data Science)")
    
    y3.add_child(math1211)
    y3.add_child(cmsc1282)
    y3.add_child(cmsc138)
    y3.add_child(cmsc161)
    y3.add_child(cmsc177)
    
    # Add prerequisites for 3rd year 2nd semester courses
    math1211.add_child(Node("Math 85"))
    cmsc1282.add_child(Node("CMSC 128.1"))
    cmsc138.add_child(Node("CMSC 125"))
    cmsc161.add_child(Node("CMSC 123"))
    cmsc161.add_child(Node("Math 120"))
    cmsc177.add_child(Node("CMSC 176"))
    cmsc177.add_child(Node("Stat 122"))
    
    # Major Course 2 options
    major2_stat = Node("Major Course 2: Stat Comp 181.1 (Linear Models in Statistical Computing I)")
    major2_hi = Node("Major Course 2: HI 193.1 (Representation and Algorithms for Computational Biochemistry)")
    
    y3.add_child(major2_stat)
    y3.add_child(major2_hi)
    
    major2_stat.add_child(Node("Stat 121"))
    major2_hi.add_child(Node("HI 191"))
    
    # =========================================================
    # ===== 4th Year - 1st Semester (Updated) =====
    # =========================================================
    cmsc141 = Node("CMSC 141 (Automata & Language Theory)")
    cmsc150 = Node("CMSC 150 (Computer Security)")
    cmsc178 = Node("CMSC 178 (Algorithm Design and Software Foundation in Data Science)")
    cmsc197 = Node("CMSC 197 (Undergraduate Seminar)")
    cmsc199 = Node("CMSC 199 (Research Methods in Computer Science)")
    elective1 = Node("Elective 1")
    
    # Major Course 3 options
    major3_stat = Node("Major Course 3: Stat Comp 183 (Multivariate Statistical Model)")
    major3_hi = Node("Major Course 3: HI HI 192 (Knowledge Representation & Health Decision Support System)")
    
    y4.add_child(cmsc141)
    y4.add_child(cmsc150)
    y4.add_child(cmsc178)
    y4.add_child(cmsc197)
    y4.add_child(cmsc199)
    y4.add_child(major3_stat)
    y4.add_child(major3_hi)
    y4.add_child(elective1)
    
    # Add prerequisites for 4th year 1st semester courses
    cmsc141.add_child(Node("CMSC 124"))
    
    cmsc150.add_child(Node("CMSC 121"))
    cmsc150.add_child(Node("CMSC 138"))
    
    cmsc178.add_child(Node("CMSC 123"))
    cmsc178.add_child(Node("CMSC 176"))
    
    cmsc197.add_child(Node("Senior Standing")) 
    cmsc199.add_child(Node("Senior Standing")) 
    
    major3_stat.add_child(Node("Stat 122"))
    major3_hi.add_child(Node("HI 191"))
    
    # =========================================================
    # ===== 4th Year - 2nd Semester (Updated) =====
    # =========================================================
    math174 = Node("Math 174 (Numerical Analysis I)")
    cmsc142 = Node("CMSC 142 (Design & Analysis of Algorithms)")
    cmsc198 = Node("CMSC 198 (Special Problem)")
    elective2 = Node("Elective 2")
    pi100 = Node("PI 100")
    
    y4.add_child(math174)
    y4.add_child(cmsc142)
    y4.add_child(cmsc198)
    y4.add_child(elective2)
    y4.add_child(pi100)
    
    # Add prerequisites for 4th year 2nd semester courses
    math174.add_child(Node("CMSC 21"))
    math174.add_child(Node("Math 121.1"))
    
    cmsc142.add_child(Node("CMSC 123"))
    
    cmsc198.add_child(Node("CMSC 197"))
    cmsc198.add_child(Node("CMSC 199"))
    
    return f


# ---------- Simple menu-driven program ----------

def main():
    print("=== COURSE PREREQUISITES VIEWER ===")
    program_forest = build_sample_forest()
    
    while True:
        print("\nMenu:")
        print("[1] View all years and courses (indented)")
        print("[2] Add a new course under a year")
        print("[3] Add a prerequisite to a course")
        print("[4] Find a course")
        print("[5] List all courses (preorder by year)")
        print("[6] Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            print("\n--- Program (by year) ---")
            program_forest.print_forest()
        
        elif choice == "2":
            print("\nWhich year do you want to add to?")
            print("[1] 1st Year")
            print("[2] 2nd Year")
            print("[3] 3rd Year")
            print("[4] 4th Year")
            year_input = input("Enter year number: ").strip()
            course_name = input("Enter new course name: ").strip()
            
            # Using the improved logic for clarity and robustness
            try:
                year_index = int(year_input) - 1
                if 0 <= year_index < len(program_forest.roots):
                    year_node = program_forest.roots[year_index]
                    year_node.add_child(Node(course_name))
                    print(f"Added '{course_name}' to {year_node.value}.")
                else:
                    print("Invalid year choice.")
            except ValueError:
                print("Invalid input. Please enter a number (1-4).")
        
        elif choice == "3":
            course_name = input("Enter the course that needs a prerequisite (exact name): ").strip()
            prereq_name = input("Enter prerequisite course name to add: ").strip()
            
            found_course = search_forest(program_forest, course_name)
            if found_course:
                found_course.add_child(Node(prereq_name))
                print(f"Added '{prereq_name}' as a prerequisite to '{course_name}'.")
            else:
                print(f"Course '{course_name}' not found.")
        
        elif choice == "4":
            name = input("Enter course name to find: ").strip()
            found = search_forest(program_forest, name)
            
            if found:
                print(f"\nCourse found: {found.value}")
                if found.children:
                    print("Direct prerequisites:")
                    for child in found.children:
                        print(f"  - {child.value}")
                else:
                    print("No prerequisites.")
            else:
                print(f"Course '{name}' not found.")
        
        elif choice == "5":
            print("\nAll courses (preorder by year):")
            for root in program_forest.roots:
                print(f"\n-- {root.value} --")
                preorder(root, lambda n: print("-", n.value))
        
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice — pick 1-6.")


if __name__ == "__main__":
    main()