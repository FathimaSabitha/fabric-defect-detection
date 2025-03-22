/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - fabric
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`fabric` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `fabric`;

/*Table structure for table `assign_order` */

DROP TABLE IF EXISTS `assign_order`;

CREATE TABLE `assign_order` (
  `assign_id` int(100) NOT NULL AUTO_INCREMENT,
  `dg_id` int(100) DEFAULT NULL,
  `om_id` int(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `assign_order` */

insert  into `assign_order`(`assign_id`,`dg_id`,`om_id`,`status`) values 
(1,1,1,'deliverd'),
(2,1,1,'deliverd'),
(3,1,1,'pending'),
(4,1,1,'pending'),
(5,5,1,'pending'),
(6,5,1,'pending'),
(7,5,1,'pending'),
(8,5,1,'pending'),
(9,5,1,'pending'),
(10,6,3,'pending');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(100) NOT NULL AUTO_INCREMENT,
  `sender_id` int(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`sender_id`,`description`,`reply`,`date`) values 
(10,19,'the fabric you send has stains ','pending','2025-02-07'),
(9,19,'there is a hole in the fabric that i ordered','pending','2025-02-07'),
(11,17,'it is damaged','pending','2025-02-08'),
(12,17,'it is damaged','we will contact you soon','2025-02-08');

/*Table structure for table `defect_report` */

DROP TABLE IF EXISTS `defect_report`;

CREATE TABLE `defect_report` (
  `report_id` int(100) NOT NULL AUTO_INCREMENT,
  `product_id` int(100) DEFAULT NULL,
  `retailer_id` int(11) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `defect_report` */

insert  into `defect_report`(`report_id`,`product_id`,`retailer_id`,`description`,`image`,`date`) values 
(17,8,4,'snags','static/a70235f8-416c-4682-8311-5bb699f64944jeans.jpg','2025-02-07'),
(16,8,4,'snags','static/488ba8d8-40c1-41e5-98a6-8d430df170d7green.jpg','2025-02-07'),
(15,8,4,'hole','static/7bf1567b-e6be-4792-a98c-65d3c9729743sab.jpg','2025-02-07'),
(13,8,4,'unknown','static/3df01e19-bbee-40d3-b97a-9f8dac590148akshi.jpg','2025-02-07'),
(14,8,4,'unknown','static/24b8324a-46a6-4e35-8bfe-b6a0cb420b03mish.jpg','2025-02-07'),
(12,4,7,'hole','static/020c20a3-2b11-4a3e-aa40-a67c61639389photopic.jpg','2025-02-07');

/*Table structure for table `delivery_agent` */

DROP TABLE IF EXISTS `delivery_agent`;

CREATE TABLE `delivery_agent` (
  `dg_id` int(100) NOT NULL AUTO_INCREMENT,
  `login_id` int(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`dg_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `delivery_agent` */

insert  into `delivery_agent`(`dg_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`address`) values 
(5,14,'Sugar','Kin','Kochi','9634875630','Kalyan House'),
(4,13,'Mohan','Kumar','Kollam','9875632140','Pulikkottil House'),
(6,15,'chris','hems','thrissur','5565112210','white house');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(100) NOT NULL AUTO_INCREMENT,
  `wholesaler_id` int(100) DEFAULT NULL,
  `retailer_id` int(100) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`wholesaler_id`,`retailer_id`,`feedback`,`date`) values 
(10,4,7,'colours are vibrant','2025-03-13'),
(11,4,7,'colours are vibrant','2025-03-13'),
(6,3,7,'It was a great fabric but there is dust in the fabric','2025-02-07'),
(9,5,7,'fabric quality is good','2025-03-13'),
(8,5,7,'Fabric quality is so low','2025-02-07'),
(12,5,7,'quality is low','2025-03-13'),
(13,5,7,'quality is low','2025-03-13');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'wholesaler','wholesaler','wholesaler'),
(3,'retailer','retailer','retailer'),
(10,'dd','dd','delivery'),
(4,'delivery_agent','delivery_agent','delivery_agent'),
(11,'www','www','wholesaler'),
(12,'rrr','rrr','retailer'),
(13,'mohan','mohank','delivery'),
(14,'sugark','sugark','delivery'),
(15,'chris','chrishems','delivery'),
(16,'Latha','latha','wholesaler'),
(17,'Misa ','Misa ','retailer'),
(18,'Vincent','vincent','retailer'),
(19,'Light','light','retailer'),
(20,'Grimmer','grimmer','retailer'),
(21,'johan','johan','retailer'),
(22,'Kenzo','kenzo','wholesaler'),
(23,'Epsilon','epsilon','wholesaler'),
(24,'Edward','edward','wholesaler'),
(25,'Megumi','megumi','wholesaler'),
(26,'Malavika','Malavika','wholesaler'),
(27,'Jonas','Jonas','retailer');

/*Table structure for table `order_details` */

DROP TABLE IF EXISTS `order_details`;

CREATE TABLE `order_details` (
  `od_id` int(100) NOT NULL AUTO_INCREMENT,
  `om_id` int(100) DEFAULT NULL,
  `product_id` int(100) DEFAULT NULL,
  `stock` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`od_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `order_details` */

insert  into `order_details`(`od_id`,`om_id`,`product_id`,`stock`,`amount`) values 
(1,1,8,'10','350'),
(2,2,13,'5','570'),
(3,2,9,'10','2500'),
(4,2,10,'12','240'),
(5,3,6,'3','200');

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `om_id` int(100) NOT NULL AUTO_INCREMENT,
  `retailer_id` int(100) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `wholesaler_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`om_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `order_master` */

insert  into `order_master`(`om_id`,`retailer_id`,`total`,`date`,`status`,`wholesaler_id`) values 
(1,4,'3500','2025-02-07','deliverd',4),
(2,7,'5590','2025-03-13','pending',5),
(3,9,'600','2025-03-13','pending',7);

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(100) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `fabric_type` varchar(100) DEFAULT NULL,
  `color` varchar(100) DEFAULT NULL,
  `price_per_unit` varchar(100) DEFAULT NULL,
  `stock_quantity` varchar(100) DEFAULT NULL,
  `minimum_order` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `wholesaler_id` int(100) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`product_name`,`description`,`category`,`fabric_type`,`color`,`price_per_unit`,`stock_quantity`,`minimum_order`,`image`,`wholesaler_id`) values 
(5,'Jute','jute fabric for stitching','fabric','jute','brownish cream','70','100','2','static/prods/eef6949c-0f0b-472c-8196-f6ba76fd55a5JUTE.jpg',3),
(4,'Frock Silk','Offwhite silk fabric','Fabric','Silk','White','50','20','2','static/prods/c16ca0c6-6e66-4605-a093-d70e766a72d3silk.jpg',3),
(6,'Rainbow Fabric','Fabric for saree','Fabric','Polyster','Rainbow','200','497','2','static/prods/be805932-a50e-4fc9-89cb-c9df7c9be3b3sim.jpg',7),
(7,'Indian Silk','Silk for saree','Fabric','Silk','Pink','2000','500','2','static/prods/c11893e2-b749-4ecf-a294-4db9cff4b84findian silk.jpg',7),
(8,'Pattern Fabric','Colourful Fabric','Pattern Fabric','Polyster','Colourful','350','990','2','static/prods/67f3de6d-5bb7-43fb-aead-c1dec87f6b1bpattern.jpg',4),
(9,'Pattern Fabric','Colourful Fabric','Pattern Fabric','cotton','Mustard yellow','250','990','2','static/prods/dc912ca1-1267-43ee-a96f-33038fb82d33pattern2.jpg',4),
(10,'rayon','rayon Fabric','Fabric','Rayon','pink, red and yellow','20','38','2','static/prods/62225ee8-254d-47dd-b53e-09f200faffa5rayon.jpg',6),
(11,'Chiffon','Chiffon Fabric','Fabric','Chiffon','pista green','96','200','2','static/prods/20f08ee5-458f-40fb-bc3e-cb13b6da4413vintage.jpg',6),
(12,'Chocolate Brown Velvet','Velvet Fabric for frock','Fabric','Velvet','Chocolate Brown','450','1000','2','static/prods/0450a905-28ad-45a2-983e-8d4b764b8cfeChocolate Brown Velvet.jpg',5),
(13,'Meter Green','Meter Green fabric for party','Party wear','Velvet','Meter Green','570','195','2','static/prods/5da5ff73-d652-409a-942d-dbe519585829Electric green Velvet.jpg',5);

/*Table structure for table `retailer` */

DROP TABLE IF EXISTS `retailer`;

CREATE TABLE `retailer` (
  `retailer_id` int(100) NOT NULL AUTO_INCREMENT,
  `login_id` int(100) DEFAULT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `owner_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `pin` varchar(100) DEFAULT NULL,
  `upload_business_license` varchar(100) DEFAULT NULL,
  `upload_tax_license` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`retailer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `retailer` */

insert  into `retailer`(`retailer_id`,`login_id`,`company_name`,`owner_name`,`email`,`phone`,`address`,`pin`,`upload_business_license`,`upload_tax_license`) values 
(6,18,'Ibotta','Vincent Thong','ibotta@gmail.com','9873601524','Maple Street,USA','963857','BusinessLicence.pdf','Tax License.pdf'),
(4,17,'AmanePvtLtd','Misa ','amane@gmail.com','9836543271','Tokyo Skytree','138849','BusinessLicence.pdf','Tax License.pdf'),
(7,19,'YagamiPvtLtd','Light Yagami','yagami@gmail.com','5896320147','Oak Avenue,USA','296011','BusinessLicence.pdf','Tax License.pdf'),
(8,20,'Wolfgang Grimmer PvtLtd','Wolfgang Grimmer','wolfgang@gmail.com','8963025741','Berlin,Deutschland','630259','BusinessLicence.pdf','Tax License.pdf'),
(9,21,'Muller PvtLtd','Johan Vilbert','muller@gmail.com','5320147896','MG Road,Bangalore','101166','BusinessLicence.pdf','Tax License.pdf'),
(10,27,'Jonasbrothers','Nick','nick@gmail.com','9441243650','nokkel house','765098','BusinessLicence.pdf','Tax License.pdf');

/*Table structure for table `wholesaler` */

DROP TABLE IF EXISTS `wholesaler`;

CREATE TABLE `wholesaler` (
  `wholesaler_id` int(100) NOT NULL AUTO_INCREMENT,
  `login_id` int(100) DEFAULT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `owner_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `pin` varchar(100) DEFAULT NULL,
  `upload_business_license` varchar(100) DEFAULT NULL,
  `upload_tax_license` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`wholesaler_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `wholesaler` */

insert  into `wholesaler`(`wholesaler_id`,`login_id`,`company_name`,`owner_name`,`email`,`phone`,`address`,`pin`,`upload_business_license`,`upload_tax_license`) values 
(4,22,'Fortner PvtLtd','Kenzo Tenma','fortner@gmail.com','8563021479','Shibuya,Tokyo','693012','BusinessLicence.pdf','Tax License.pdf'),
(3,16,'Birlo Company Pvt.Ltd','Latha','latha@gmail.com','9632584105','Maliyekkal house','680002','buisness_license.docx','Tax_License.docx'),
(5,23,'Epsilon PvtLtd','Epsilon','epsilon@gmail.com','9463021752','Delhi,India','852963','BusinessLicence.pdf','Tax License.pdf'),
(6,24,'Edward PvtLtd','Edward Elric','edward@gmail.com','7863012547','Amestris, Central Region','123654','BusinessLicence.pdf','Tax License.pdf'),
(7,25,'Oiwa PvtLtd','Megumi Oiwa','oiwa@gmail.com','4528963178','Zurich, Switzerland','964512','BusinessLicence.pdf','Tax License.pdf'),
(8,26,'MM','Malavika','malavika@gmail.com','944557329','chowallur house','680308','buisness_license.docx','Tax_License.docx');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
