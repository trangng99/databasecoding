-- Write your own SQL object definition here, and it'll be included in your package.
CREATE SCHEMA S;
GO 

CREATE TABLE S.Student (
  student_id INT PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  education_level VARCHAR(255),
  student_number VARCHAR (255),
  personal_email VARCHAR(255),
  school_email VARCHAR(255),
  student_gender VARCHAR(255),
  student_DOB DATETIME2,
  nationality VARCHAR(255)
);

CREATE TABLE S.Landlord_Type (
  landlord_type_id INT PRIMARY KEY,
  landlord_type_name VARCHAR(255)
);

CREATE TABLE S.Room_Type (
  room_type_id INT PRIMARY KEY,
  room_type VARCHAR(255)
);

CREATE TABLE S.Rental_Agent (
  rental_agent_id INT PRIMARY KEY,
  rental_agent_first_name VARCHAR(255),
  rental_agent_last_name VARCHAR(255),
  email VARCHAR(255),
  phone_number VARCHAR (255)
);

CREATE TABLE S.ContractLength (
  contract_length_id INT PRIMARY KEY,
  contract_length INT
);

CREATE TABLE S.Landlord (
  landlord_id INT PRIMARY KEY,
  landlord_type_id INT,
  landlord_first_name VARCHAR(255),
  landlord_last_name VARCHAR(255),
  landlord_gender VARCHAR(255),
  landlord_email VARCHAR(255),
  landlord_phone_number VARCHAR(255),
  FOREIGN KEY (landlord_type_id) REFERENCES S.Landlord_Type(landlord_type_id)
);

CREATE TABLE S.Residence (
  residence_id INT PRIMARY KEY,
  landlord_id INT,
  is_catered BIT,
  residence_name VARCHAR(255),
  total_rooms_available INT,
  is_central_social_space BIT,
  is_cleaning_provision BIT,
  residence_postcode VARCHAR(255),
  FOREIGN KEY (landlord_id) REFERENCES S.Landlord(landlord_id)
);

CREATE TABLE S.Residence_RoomType (
  residence_roomtype_id INT PRIMARY KEY,
  room_type_id INT,
  residence_id INT,
  fee INT,
  FOREIGN KEY (room_type_id) REFERENCES S.Room_Type(room_type_id),
  FOREIGN KEY (residence_id) REFERENCES S.Residence(residence_id)
);

CREATE TABLE S.Student_Residence_Option (
  residence_option_id INT PRIMARY KEY,
  student_id INT,
  contract_length_id INT,
  residence_roomtype_id INT,
  residence_priority INT,
  date_created DATETIME,
  FOREIGN KEY (student_id) REFERENCES S.Student(student_id),
  FOREIGN KEY (contract_length_id) REFERENCES S.ContractLength(contract_length_id),
  FOREIGN KEY (residence_roomtype_id) REFERENCES S.Residence_RoomType(residence_roomtype_id)
);

CREATE TABLE S.Room (
  room_id INT PRIMARY KEY,
  residence_roomtype_id INT,
  contract_length_id INT,
  room_number INT,
  FOREIGN KEY (residence_roomtype_id) REFERENCES S.Residence_RoomType(residence_roomtype_id),
  FOREIGN KEY (contract_length_id) REFERENCES S.ContractLength(contract_length_id)
);

CREATE TABLE S.Student_Contract (
  student_contract_id INT PRIMARY KEY,
  rental_agent_id INT,
  student_id INT,
  room_id INT,
  offer_paid_on DATETIME,
  arrival_date DATETIME,
  departure_date DATETIME,
  FOREIGN KEY (rental_agent_id) REFERENCES S.Rental_Agent(rental_agent_id),
  FOREIGN KEY (student_id) REFERENCES S.Student(student_id),
  FOREIGN KEY (room_id) REFERENCES S.Room(room_id)
);

-- Relationships

ALTER TABLE S.Student_Residence_Option
ADD CONSTRAINT FK_Student_Residence_Option_Student FOREIGN KEY (student_id) REFERENCES S.Student(student_id);

ALTER TABLE S.Student_Residence_Option
ADD CONSTRAINT FK_Student_Residence_Option_ContractLength FOREIGN KEY (contract_length_id) REFERENCES S.ContractLength(contract_length_id);

ALTER TABLE S.Student_Residence_Option
ADD CONSTRAINT FK_Student_Residence_Option_Residence_RoomType FOREIGN KEY (residence_roomtype_id) REFERENCES S.Residence_RoomType(residence_roomtype_id);

ALTER TABLE S.Room
ADD CONSTRAINT FK_Room_Residence_RoomType FOREIGN KEY (residence_roomtype_id) REFERENCES S.Residence_RoomType(residence_roomtype_id);

ALTER TABLE S.Room
ADD CONSTRAINT FK_Room_ContractLength FOREIGN KEY (contract_length_id) REFERENCES S.ContractLength(contract_length_id);

ALTER TABLE S.Student_Contract
ADD CONSTRAINT FK_Student_Contract_Rental_Agent FOREIGN KEY (rental_agent_id) REFERENCES S.Rental_Agent(rental_agent_id);

ALTER TABLE S.Student_Contract
ADD CONSTRAINT FK_Student_Contract_Student FOREIGN KEY (student_id) REFERENCES S.Student(student_id);

ALTER TABLE S.Student_Contract
ADD CONSTRAINT FK_Student_Contract_Room FOREIGN KEY (room_id) REFERENCES S.Room(room_id);

ALTER TABLE S.Landlord
ADD CONSTRAINT FK_Landlord_Landlord_Type FOREIGN KEY (landlord_type_id) REFERENCES S.Landlord_Type(landlord_type_id);

ALTER TABLE S.Residence
ADD CONSTRAINT FK_Residence_Landlord FOREIGN KEY (landlord_id) REFERENCES S.Landlord(landlord_id);

ALTER TABLE S.Residence_RoomType
ADD CONSTRAINT FK_Residence_RoomType_Room_Type FOREIGN KEY (room_type_id) REFERENCES S.Room_Type(room_type_id);

ALTER TABLE S.Residence_RoomType
ADD CONSTRAINT FK_Residence_RoomType_Residence FOREIGN KEY (residence_id) REFERENCES S.Residence(residence_id);