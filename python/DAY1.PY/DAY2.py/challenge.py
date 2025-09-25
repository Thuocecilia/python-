import pandas as pd
import os
from datetime import datetime

class MedicalRecordsSystem:
    def __init__(self, filename="patients.csv"):
        self.filename = filename
        # Create CSV with headers if it doesn't exist
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=["PatientID", "FullName", "Age", "Gender", "Diagnosis", "DateOfVisit"])
            df.to_csv(self.filename, index=False)

    def load_data(self):
        """Load CSV into DataFrame."""
        return pd.read_csv(self.filename)

    def save_data(self, df):
        """Save DataFrame to CSV."""
        df.to_csv(self.filename, index=False)

    def add_patient(self):
        try:
            df = self.load_data()
            patient_id = input("Enter Patient ID: ").strip()
            if patient_id in df["PatientID"].astype(str).values:
                print("Error: Patient ID already exists.")
                return

            full_name = input("Enter Full Name: ").strip()
            
            # Validate age input
            while True:
                try:
                    age = int(input("Enter Age: ").strip())
                    break
                except ValueError:
                    print("Invalid input! Age must be an integer.")

            gender = input("Enter Gender (Male/Female): ").strip()
            diagnosis = input("Enter Diagnosis: ").strip()
            date_of_visit = datetime.today().strftime("%Y-%m-%d")

            new_patient = {
                "PatientID": patient_id,
                "FullName": full_name,
                "Age": age,
                "Gender": gender,
                "Diagnosis": diagnosis,
                "DateOfVisit": date_of_visit
            }

            df = pd.concat([df, pd.DataFrame([new_patient])], ignore_index=True)
            self.save_data(df)
            print(f"Patient {full_name} added successfully!")

        except Exception as e:
            print(f"Error adding patient: {e}")

    def view_patients(self):
        try:
            df = self.load_data()
            if df.empty:
                print("No patient records found.")
            else:
                print(df.to_string(index=False))
        except Exception as e:
            print(f"Error viewing patients: {e}")

    def search_patient(self):
        try:
            df = self.load_data()
            patient_id = input("Enter Patient ID to search: ").strip()
            patient = df[df["PatientID"].astype(str) == patient_id]
            if patient.empty:
                print("No patient found with that ID.")
            else:
                print(patient.to_string(index=False))
        except Exception as e:
            print(f"Error searching patient: {e}")

    def edit_patient(self):
        try:
            df = self.load_data()
            patient_id = input("Enter Patient ID to edit: ").strip()
            index = df[df["PatientID"].astype(str) == patient_id].index
            if len(index) == 0:
                print("No patient found with that ID.")
                return
            index = index[0]

            print("Press Enter to leave a field unchanged.")
            full_name = input(f"Full Name [{df.at[index, 'FullName']}]: ").strip()
            age_input = input(f"Age [{df.at[index, 'Age']}]: ").strip()
            gender = input(f"Gender [{df.at[index, 'Gender']}]: ").strip()
            diagnosis = input(f"Diagnosis [{df.at[index, 'Diagnosis']}]: ").strip()

            if full_name:
                df.at[index, 'FullName'] = full_name
            if age_input:
                try:
                    df.at[index, 'Age'] = int(age_input)
                except ValueError:
                    print("Invalid age input, keeping previous value.")
            if gender:
                df.at[index, 'Gender'] = gender
            if diagnosis:
                df.at[index, 'Diagnosis'] = diagnosis

            self.save_data(df)
            print(f"Patient {patient_id} updated successfully!")
        except Exception as e:
            print(f"Error editing patient: {e}")

    def delete_patient(self):
        try:
            df = self.load_data()
            patient_id = input("Enter Patient ID to delete: ").strip()
            if patient_id not in df["PatientID"].astype(str).values:
                print("No patient found with that ID.")
                return
            df = df[df["PatientID"].astype(str) != patient_id]
            self.save_data(df)
            print(f"Patient {patient_id} deleted successfully!")
        except Exception as e:
            print(f"Error deleting patient: {e}")

    def run(self):
        print("Welcome to the Medical Records System!")
        while True:
            print("\nOptions: add | view | search | edit | delete | exit")
            choice = input("Enter command: ").strip().lower()
            if choice == "add":
                self.add_patient()
            elif choice == "view":
                self.view_patients()
            elif choice == "search":
                self.search_patient()
            elif choice == "edit":
                self.edit_patient()
            elif choice == "delete":
                self.delete_patient()
            elif choice == "exit":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid command. Try again.")

# ===== Example Usage =====
if __name__ == "__main__":
    system = MedicalRecordsSystem()
    system.run()
