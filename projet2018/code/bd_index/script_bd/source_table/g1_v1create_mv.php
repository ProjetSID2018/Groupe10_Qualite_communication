<?php
# Creation of tables
# Group supervision : Loann Michon and Florence Canal

# Login connexion
include '../../../utils/connexion.php';

try {
	// connexion to the database
    $conn = new PDO("mysql:host=localhost;dbname=DBIndex", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    #------------------------------------------------------------
	# Vue materialisée : mv_number_article_week
	#------------------------------------------------------------
    $sql = "CREATE TABLE IF NOT EXISTS `mv_number_article_week` (
  `number_article` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;";
    // use exec() because no results are returned
    $conn->exec($sql);
    echo "<h2>mv_number_article_week created successfully</h2>";  

    #------------------------------------------------------------
	# Vue materialisée : mv_number_article_week_label
	#------------------------------------------------------------
    $sql = "CREATE TABLE IF NOT EXISTS `mv_number_article_week_label` (
  `id_label` int(11) NOT NULL,
  `number_article` int(11) NOT NULL,
  PRIMARY KEY (`id_label`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ADD CONSTRAINT `fk_article_label` FOREIGN KEY (`id_label`) REFERENCES `label` (`id_label`) ON DELETE CASCADE ON UPDATE CASCADE;";
    // use exec() because no results are returned
    $conn->exec($sql);
    echo "<h2>mv_number_article_week_label created successfully</h2>";  

    #------------------------------------------------------------
	# Vue materialisée : mv Calcul TF-IDF par jour
	#------------------------------------------------------------
    $sql = "CREATE TABLE IF NOT EXISTS `mv_term_frequency_day` (
  `date_publication` date NOT NULL,
  `id_word` int(11) NOT NULL,
  `id_article` int(11) NOT NULL,
  `frequency` int(11) NOT NULL,
  PRIMARY KEY (`date_publication`,`id_word`,`id_article`),
  KEY `fk_word_tf_day` (`id_word`),
  KEY `fk_article_tf_day` (`id_article`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_term_frequency_day`
  ADD CONSTRAINT `fk_article_tf_day` FOREIGN KEY (`id_article`) REFERENCES `article` (`id_article`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_word_tf_day` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE IF NOT EXISTS `nb_articles` (
  `date_publication` date NOT NULL,
  `nb_article` int(11) NOT NULL,
  PRIMARY KEY (`date_publication`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `nb_articles_word` (
  `date_publication` date NOT NULL,
  `id_word` int(11) NOT NULL,
  `nb_articles` int(11) NOT NULL,
  PRIMARY KEY (`date_publication`,`id_word`),
  KEY `fk_word_nb_articles_word_day` (`id_word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `nb_articles_word`
  ADD CONSTRAINT `fk_word_nb_articles_word_day` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE IF NOT EXISTS `mv_inverse_document_frequency_day` (
  `date_publication` date NOT NULL,
  `id_word` int(11) NOT NULL,
  `idf` float NOT NULL,
  PRIMARY KEY (`date_publication`,`id_word`),
  KEY `fk_word_idf` (`id_word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_inverse_document_frequency_day`
  ADD CONSTRAINT `fk_word_idf` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;
  CREATE TABLE IF NOT EXISTS `mv_tf_idf_day` (
  `date_publication` date NOT NULL,
  `id_word` int(11) NOT NULL,
  `id_articles` int(11) NOT NULL,
  `tf` int(11) NOT NULL,
  `tf_idf` float NOT NULL,
  PRIMARY KEY (`date_publication`,`id_word`,`id_articles`),
  KEY `fk_word_tf_idf_day` (`id_word`),
  KEY `fk_article_tf_idf_day` (`id_articles`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `mv_tf_idf_day`
  ADD CONSTRAINT `fk_article_tf_idf_day` FOREIGN KEY (`id_articles`) REFERENCES `article` (`id_article`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD CONSTRAINT `fk_word_tf_idf_day` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;";
    // use exec() because no results are returned
    $conn->exec($sql);
    echo "<h2>mv Calcul TF-IDF par jour created successfully</h2>";  

    #------------------------------------------------------------
	# Vue materialisée : mv tf_idf par semaine
	#------------------------------------------------------------
    $sql = "CREATE TABLE IF NOT EXISTS `mv_term_frequency_week` (
  `id_word` int(11) NOT NULL,
  `id_article` int(11) NOT NULL,
  `frequency` int(11) NOT NULL,
  PRIMARY KEY (`id_word`,`id_article`),
  KEY `fk_article_tf_week` (`id_article`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_term_frequency_week`
  ADD CONSTRAINT `fk_article_tf_week` FOREIGN KEY (`id_article`) REFERENCES `article` (`id_article`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_word_tf_week` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE IF NOT EXISTS `nb_articles_week` (
  `nb_articles` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `nb_articles_word_week` (
  `id_word` int(11) NOT NULL,
  `nb_articles` int(11) NOT NULL,
  PRIMARY KEY (`id_word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `nb_articles_word_week`
  ADD CONSTRAINT `fk_word_nb_articles_word_week` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE IF NOT EXISTS `mv_inverse_document_frequency_week` (
  `id_word` int(11) NOT NULL,
  `idf` float NOT NULL,
  PRIMARY KEY (`id_word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_inverse_document_frequency_week`
  ADD CONSTRAINT `fk_word_idf_week` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;


CREATE TABLE IF NOT EXISTS `mv_tf_idf_week` (
  `date_publication` date NOT NULL,
  `id_word` int(11) NOT NULL,
  `id_article` int(11) NOT NULL,
  `tf` int(11) NOT NULL,
  `tf_idf` float NOT NULL,
  PRIMARY KEY (`date_publication`,`id_word`,`id_article`),
  KEY `fk_word_tf_idf_week` (`id_word`),
  KEY `fk_article_tf_idf_week` (`id_article`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_tf_idf_week`
  ADD CONSTRAINT `fk_article_tf_idf_week` FOREIGN KEY (`id_article`) REFERENCES `article` (`id_article`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD CONSTRAINT `fk_word_tf_idf_week` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;";

    #------------------------------------------------------------
	# Vue materialisée : mv tf_idf par mois
	#------------------------------------------------------------
    $sql = "CREATE TABLE IF NOT EXISTS `mv_term_frequency_month` (
  `id_word` int(11) NOT NULL,
  `id_article` int(11) NOT NULL,
  `frequency` int(11) NOT NULL,
  PRIMARY KEY (`id_word`,`id_article`),
  KEY `fk_article_tf_month` (`id_article`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_term_frequency_month`
  ADD CONSTRAINT `fk_article_tf_month` FOREIGN KEY (`id_article`) REFERENCES `article` (`id_article`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_word_tf_month` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE IF NOT EXISTS `nb_articles_month` (
  `nb_articles` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `nb_articles_word_month` (
  `id_word` int(11) NOT NULL,
  `nb_articles` int(11) NOT NULL,
  PRIMARY KEY (`id_word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `nb_articles_word_month`
  ADD CONSTRAINT `fk_word_nb_articles_word_month` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE IF NOT EXISTS `mv_inverse_document_frequency_month` (
  `id_word` int(11) NOT NULL,
  `idf` float NOT NULL,
  PRIMARY KEY (`id_word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_inverse_document_frequency_month`
  ADD CONSTRAINT `fk_word_idf_month` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;
 

CREATE TABLE IF NOT EXISTS `mv_tf_idf_month` (
  `date_publication` date NOT NULL,
  `id_word` int(11) NOT NULL,
  `id_article` int(11) NOT NULL,
  `tf` int(11) NOT NULL,
  `tf_idf` float NOT NULL,
  PRIMARY KEY (`date_publication`,`id_word`,`id_article`),
  KEY `fk_article_tf_idf_month` (`id_article`),
  KEY `fk_word_tf_idf_month` (`id_word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_tf_idf_month`
  ADD CONSTRAINT `fk_article_tf_idf_month` FOREIGN KEY (`id_article`) REFERENCES `article` (`id_article`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD CONSTRAINT `fk_word_tf_idf_month` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;";
    // use exec() because no results are returned
    $conn->exec($sql);
    echo "<h2>mv tf_idf par mois created successfully</h2>";  


    #------------------------------------------------------------
	# Vue materialisée : mv tf_idf par periode
	#------------------------------------------------------------
    $sql = "CREATE TABLE IF NOT EXISTS `mv_term_frequency_period` (
  `id_word` int(11) NOT NULL,
  `id_article` int(11) NOT NULL,
  `frequency` int(11) NOT NULL,
  PRIMARY KEY (`id_word`,`id_article`),
  KEY `fk_article_tf_period` (`id_article`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_term_frequency_period`
  ADD CONSTRAINT `fk_article_tf_period` FOREIGN KEY (`id_article`) REFERENCES `article` (`id_article`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_word_tf_period` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE IF NOT EXISTS `nb_articles_period` (
  `nb_articles` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `nb_articles_word_period` (
  `id_word` int(11) NOT NULL,
  `nb_articles` int(11) NOT NULL,
  PRIMARY KEY (`id_word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `nb_articles_word_period`
  ADD CONSTRAINT `fk_word_nb_articles_word_period` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE IF NOT EXISTS `mv_inverse_document_frequency_period` (
  `id_word` int(11) NOT NULL,
  `idf` float NOT NULL,
  PRIMARY KEY (`id_word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_inverse_document_frequency_period`
  ADD CONSTRAINT `fk_word_idf_period` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE IF NOT EXISTS `mv_tf_idf_period` (
  `date_debut_period` date NOT NULL,
  `date_fin_period` date NOT NULL,
  `date_publication` date NOT NULL,
  `id_word` int(11) NOT NULL,
  `id_article` int(11) NOT NULL,
  `tf` int(11) NOT NULL,
  `tf_idf` float NOT NULL,
  PRIMARY KEY (`date_publication`,`id_word`,`id_article`),
  KEY `fk_word_tf_idf_period` (`id_word`),
  KEY `fk_article_tf_idf_period` (`id_article`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_tf_idf_period`
  ADD CONSTRAINT `fk_article_tf_idf_period` FOREIGN KEY (`id_article`) REFERENCES `article` (`id_article`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD CONSTRAINT `fk_word_tf_idf_period` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;";
    // use exec() because no results are returned
    $conn->exec($sql);
    echo "<h2>mv tf_idf par periode created successfully</h2>";  


    // use exec() because no results are returned
    $conn->exec($sql);
    echo "<h2>mv tf_idf par semaine created successfully</h2>";    

  
    }
catch(PDOException $e)
    {
    echo  $e->getMessage();
    }
$conn = null;
?>
