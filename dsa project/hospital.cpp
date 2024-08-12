#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

// Define a structure for storing patient information
struct Patient {
    int id;
    string name;
    int age;
    string gender;
    string disease;
};

class Hospital {
private:
    vector<Patient> patients;
    int nextId;

public:
    Hospital() : nextId(1) {
        // Load patient data from file on initialization
        loadPatientsFromFile("patients.txt");
    }

    ~Hospital() {
        // Save patient data to file before exiting
        savePatientsToFile("patients.txt");
    }

    // Function to add a new patient
    void addPatient() {
        Patient p;
        p.id = nextId++;
        cout << "Enter patient name: ";
        cin >> p.name;
        cout << "Enter patient age: ";
        cin >> p.age;
        cout << "Enter patient gender: ";
        cin >> p.gender;
        cout << "Enter patient disease: ";
        cin >> p.disease;
        patients.push_back(p);
        cout << "Patient added successfully with ID: " << p.id << endl;
    }

    // Function to display all patients
    void displayPatients() {
        if (patients.empty()) {
            cout << "No patients found." << endl;
            return;
        }
        cout << "----- List of Patients -----" << endl;
        for (const auto& patient : patients) {
            cout << "ID: " << patient.id << ", Name: " << patient.name << ", Age: " << patient.age << ", Gender: " << patient.gender << ", Disease: " << patient.disease << endl;
        }
        cout << "---------------------------" << endl;
    }

    // Function to search for a patient by ID
    void searchPatient(int id) {
        for (const auto& patient : patients) {
            if (patient.id == id) {
                cout << "ID: " << patient.id << ", Name: " << patient.name << ", Age: " << patient.age << ", Gender: " << patient.gender << ", Disease: " << patient.disease << endl;
                return;
            }
        }
        cout << "Patient with ID " << id << " not found." << endl;
    }

    // Function to delete a patient record by ID
    void deletePatient(int id) {
        for (auto it = patients.begin(); it != patients.end(); ++it) {
            if (it->id == id) {
                patients.erase(it);
                cout << "Patient with ID " << id << " deleted successfully." << endl;
                return;
            }
        }
        cout << "Patient with ID " << id << " not found." << endl;
    }

    // Function to load patient data from file
    void loadPatientsFromFile(const string& filename) {
        ifstream file(filename);
        if (file.is_open()) {
            Patient p;
            while (file >> p.id >> p.name >> p.age >> p.gender >> p.disease) {
                patients.push_back(p);
                if (p.id >= nextId) {
                    nextId = p.id + 1;
                }
            }
            file.close();
        } else {
            cout << "Unable to open file " << filename << ". Starting with empty patient list." << endl;
        }
    }

    // Function to save patient data to file
    void savePatientsToFile(const string& filename) {
        ofstream file(filename);
        if (file.is_open()) {
            for (const auto& patient : patients) {
                file << patient.id << " " << patient.name << " " << patient.age << " " << patient.gender << " " << patient.disease << endl;
            }
            file.close();
        } else {
            cout << "Unable to save patient data to file " << filename << "." << endl;
        }
    }
};

int main() {
    Hospital hospital;
    int choice;
    int id;

    do {
        cout << "----- Hospital Management System -----" << endl;
        cout << "1. Add Patient" << endl;
        cout << "2. Display All Patients" << endl;
        cout << "3. Search Patient" << endl;
        cout << "4. Delete Patient Record" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch(choice) {
            case 1:
                hospital.addPatient();
                break;
            case 2:
                hospital.displayPatients();
                break;
            case 3:
                cout << "Enter patient ID to search: ";
                cin >> id;
                hospital.searchPatient(id);
                break;
            case 4:
                cout << "Enter patient ID to delete: ";
                cin >> id;
                hospital.deletePatient(id);
                break;
            case 5:
                cout << "Exiting..." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while(choice != 5);

    return 0;
}
