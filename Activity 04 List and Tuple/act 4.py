import json

class StudentRecordManager:
    def __init__(self):
        self.records = []  # Dito ko ilalagay lahat ng student records
        self.file_name = None  # Para malaman kung anong file yung currently ginagamit

    def open_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.records = json.load(file)  # I-load yung laman ng file papunta sa records
            self.file_name = file_name  # I-set yung file name na ginagamit
            print("File opened successfully.")
        except Exception as e:
            print(f"Error opening file: {e}")  # Kung may error, ipapakita lang

    def save_file(self):
        if self.file_name:
            self.save_to_file(self.file_name)  # I-save sa existing file
        else:
            print("No file to save. Use 'Save As' to specify a file.")  # Walang existing file, kaya dapat "Save As"

    def save_as_file(self, file_name):
        self.save_to_file(file_name)  # I-save yung records sa bagong file name

    def save_to_file(self, file_name):
        try:
            with open(file_name, 'w') as file:
                json.dump(self.records, file)  # Isusulat lahat ng records sa file
            self.file_name = file_name  # Update yung file name
            print("File saved successfully.")
        except Exception as e:
            print(f"Error saving file: {e}")  # Error message pag di na-save

    def show_all_students(self):
        for record in self.records:  # I-loop lahat ng student records
            print(record)  # I-print bawat record

    def order_by_last_name(self):
        self.records.sort(key=lambda x: x['name'][1])  # I-sort yung records gamit yung last name
        print("Records ordered by last name.")

    def order_by_grade(self):
        # Compute muna yung final grade bago i-sort
        for record in self.records:
            record['final_grade'] = (0.6 * record['class_standing']) + (0.4 * record['major_exam_grade'])
        self.records.sort(key=lambda x: x['final_grade'], reverse=True)  # I-sort by final grade (highest to lowest)
        print("Records ordered by grade.")

    def show_student_record(self, student_id):
        for record in self.records:
            if record['id'] == student_id:  # Hanapin yung student record gamit yung ID
                print(record)
                return
        print("Student record not found.")  # Kung wala, sabihin na di nahanap

    def add_record(self, student_id, name, class_standing, major_exam_grade):
        if len(student_id) != 6 or not student_id.isdigit():  # Check kung valid yung student ID (6 digits)
            print("Student ID must be a six-digit number.")
            return
        self.records.append({  # Mag-a-add ng bagong record sa list
            'id': student_id,
            'name': tuple(name.split()),  # Gawing tuple yung name (first name, last name)
            'class_standing': class_standing,
            'major_exam_grade': major_exam_grade
        })
        print("Record added.")

    def edit_record(self, student_id, name=None, class_standing=None, major_exam_grade=None):
        for record in self.records:
            if record['id'] == student_id:  # Hanapin kung may match na student ID
                if name:
                    record['name'] = tuple(name.split())  # Palitan yung pangalan kung may bagong input
                if class_standing is not None:
                    record['class_standing'] = class_standing  # Palitan yung class standing grade kung may input
                if major_exam_grade is not None:
                    record['major_exam_grade'] = major_exam_grade  # Palitan yung major exam grade kung may input
                print("Record updated.")
                return
        print("Student record not found.")  # Kung wala, sabihin na di nahanap

    def delete_record(self, student_id):
        for record in self.records:
            if record['id'] == student_id:  # Hanapin yung record gamit yung ID
                self.records.remove(record)  # Burahin kung meron
                print("Record deleted.")
                return
        print("Student record not found.")  # Kung wala, sabihin na di nahanap

def main():
    manager = StudentRecordManager()
    
    while True:
        # Menu options
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("0. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            file_name = input("Enter filename to open: ")  # Hihingi ng file name
            manager.open_file(file_name)
        elif choice == '2':
            manager.save_file()  # I-save yung file
        elif choice == '3':
            file_name = input("Enter filename to save as: ")  # Hihingi ng bagong file name
            manager.save_as_file(file_name)
        elif choice == '4':
            manager.show_all_students()  # Ipakita lahat ng student records
        elif choice == '5':
            manager.order_by_last_name()  # I-sort by last name
        elif choice == '6':
            manager.order_by_grade()  # I-sort by grade
        elif choice == '7':
            student_id = input("Enter student ID to view: ")  # Hihingi ng student ID
            manager.show_student_record(student_id)
        elif choice == '8':
            student_id = input("Enter student ID (6 digits): ")  # Hihingi ng student ID
            name = input("Enter student name (first and last): ")  # Hihingi ng pangalan
            class_standing = float(input("Enter class standing grade: "))  # Hihingi ng class standing grade
            major_exam_grade = float(input("Enter major exam grade: "))  # Hihingi ng major exam grade
            manager.add_record(student_id, name, class_standing, major_exam_grade)  # I-add yung record
        elif choice == '9':
            student_id = input("Enter student ID to edit: ")  # Hihingi ng student ID
            name = input("Enter new student name (or leave blank to keep current): ")  # Hihingi ng bagong pangalan kung meron
            class_standing = input("Enter new class standing grade (or leave blank to keep current): ")  # Hihingi ng bagong class standing grade kung meron
            major_exam_grade = input("Enter new major exam grade (or leave blank to keep current): ")  # Hihingi ng bagong major exam grade kung meron
            manager.edit_record(student_id, name, 
                                float(class_standing) if class_standing else None,
                                float(major_exam_grade) if major_exam_grade else None)  # I-edit yung record
        elif choice == '10':
            student_id = input("Enter student ID to delete: ")  # Hihingi ng student ID para burahin
            manager.delete_record(student_id)  # I-delete yung record
        elif choice == '0':
            break  # Exit sa loop
        else:
            print("Invalid choice, please try again.")  # Kung mali yung input, ulitin lang

if __name__ == "__main__":
    main()  # Tawagin yung main function para mag-run yung program
