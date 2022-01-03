CREATE DATABASE IF NOT EXISTS `demo` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `demo`;

CREATE TABLE IF NOT EXISTS `demo`.`accounts`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `role` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8;

INSERT INTO `accounts` (`id`, `username`, `password`, `email`, `role`) VALUES (1, 'admin', 'admin', 'admin@test.com', '1');
INSERT INTO `accounts` (`username`, `password`, `email`, `role`)  VALUES 
("Justin Crosby","JKK84ACM5RT","nisi.magna.sed@protonmail.couk",0),
("Preston Petty","SOV13CKZ6WO","nullam.enim.sed@icloud.ca",0),
("Erasmus Small","OWM24YUK0BG","ullamcorper.duis@icloud.com",0),
("Patrick Whitfield","MBD96ZUU2QS","rhoncus.id.mollis@aol.ca",0),
("Ezra Levine","OYT32IPY6MO","ante.bibendum.ullamcorper@outlook.org",0),
("Emily Patel","JFY87LTS2LD","in.lorem@hotmail.ca",1),
("Hadassah Glenn","TQE71YCY6EC","ut.cursus.luctus@google.com",0),
("Ross Sutton","HCK51PKH4SN","tincidunt.neque@icloud.com",1),
("Felix Roberson","YLQ95RFP6DH","vitae.velit@hotmail.couk",1),
("Leroy Delaney","UIY46GMC7GZ","ac.mi.eleifend@outlook.ca",0),
("Lee Turner","FBE26NOW3GD","eu.enim@aol.com",1),
("Keefe Mason","WQE65JSF9AQ","et.tristique@aol.com",1),
("Eric Wilkinson","EBR07KWF5NN","penatibus.et@yahoo.edu",1),

