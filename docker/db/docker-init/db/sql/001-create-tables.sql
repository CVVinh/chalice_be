-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: pclcm_mysql
-- Generation Time: Jun 06, 2023 at 01:36 AM
-- Server version: 8.0.23
-- PHP Version: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_for_base`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('d12a3250a04c');

-- --------------------------------------------------------

--
-- Table structure for table `m_accounts`
--

CREATE TABLE `m_accounts` (
  `account_id` int NOT NULL COMMENT 'アカウントID',
  `account_cd` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'アカウントコード:社員番号など利用企業のIDやコードのため',
  `ext_account_id` int DEFAULT NULL COMMENT '外部アカウントID:cognitoなどの外部認証サービスと連携する場合は設定',
  `account_name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'アカウント名',
  `email_address` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'メールアドレス',
  `account_status` int NOT NULL DEFAULT '0' COMMENT 'ステータス:0：仮登録、1：本登録、2：削除',
  `is_system_manager` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'システム管理フラグ:アプリケーションで設定/更新しないこと',
  `version` int NOT NULL DEFAULT '1' COMMENT 'バージョン:楽観的排他で利用',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時:プログラムでは設定しない',
  `created_by` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '作成処理:プログラムで設定、API名、関数名',
  `modified_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新日時:プログラムでは設定しない',
  `modified_by` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '更新処理:プログラムで設定、API名、関数名',
  `deleted_at` datetime DEFAULT NULL COMMENT '削除日時',
  `deleted_by` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '削除',
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0' COMMENT '登録旗deleted: 0：消去未 ,1：消去済'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `m_account_base`
--

CREATE TABLE `m_account_base` (
  `account_base_id` int NOT NULL COMMENT 'アカウントベースID',
  `account_id` int DEFAULT NULL COMMENT 'アカウントID',
  `base_id` int DEFAULT NULL COMMENT '拠点ID',
  `version` int NOT NULL DEFAULT '1' COMMENT 'バージョン:楽観的排他で利用',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時:プログラムでは設定しない',
  `created_by` int DEFAULT NULL COMMENT '作成処理:プログラムで設定、API名、関数名',
  `modified_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新日時:プログラムでは設定しない',
  `modified_by` int DEFAULT NULL COMMENT '更新処理:プログラムで設定、API名、関数名',
  `deleted_at` datetime DEFAULT NULL COMMENT '削除日時',
  `deleted_by` int DEFAULT NULL COMMENT '削除者',
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0' COMMENT '登録旗deleted: 0：消去未 ,1：消去済'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `m_base`
--

CREATE TABLE `m_base` (
  `base_id` int NOT NULL COMMENT '拠点ID',
  `base_cd` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '拠点コード',
  `base_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '拠点名',
  `zip_code` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '郵便番号',
  `pref_code` int NOT NULL COMMENT '都道府県コード',
  `address` varchar(400) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '住所',
  `addressee` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '受取名:配送や郵送時の受信名',
  `telephone_number` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '電話番号',
  `fax_number` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'FAX番号',
  `e_mail_address` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'メールアドレス',
  `note` text COLLATE utf8mb4_unicode_ci COMMENT '備考',
  `version` int NOT NULL DEFAULT '1' COMMENT 'バージョン:楽観的排他で利用',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時:プログラムでは設定しない',
  `created_by` int DEFAULT NULL COMMENT '作成処理:プログラムで設定、API名、関数名',
  `modified_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新日時:プログラムでは設定しない',
  `modified_by` int DEFAULT NULL COMMENT '更新処理:プログラムで設定、API名、関数名',
  `deleted_at` datetime DEFAULT NULL COMMENT '削除日時',
  `deleted_by` int DEFAULT NULL COMMENT '削除者',
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0' COMMENT '登録旗deleted: 0：消去未 ,1：消去済'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `m_insurances`
--

CREATE TABLE `m_insurances` (
  `insurance_id` int NOT NULL COMMENT '保険ID',
  `insurance_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前保険'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `m_makers`
--

CREATE TABLE `m_makers` (
  `maker_id` int NOT NULL COMMENT 'メーカーID',
  `maker_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前メーカー'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `m_options`
--

CREATE TABLE `m_options` (
  `option_id` int NOT NULL COMMENT 'オプションID',
  `option_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前オプション'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `m_payment_methods`
--

CREATE TABLE `m_payment_methods` (
  `payment_method_id` int NOT NULL COMMENT '保険ID',
  `payment_method_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前保険'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `m_prefecture`
--

CREATE TABLE `m_prefecture` (
  `pref_id` int NOT NULL COMMENT '県ID',
  `pref_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前県'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `m_stores`
--

CREATE TABLE `m_stores` (
  `store_id` int NOT NULL COMMENT '売上ID',
  `store_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前売上'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `m_vehicles`
--

CREATE TABLE `m_vehicles` (
  `vehicle_id` int NOT NULL COMMENT '車両ID',
  `vehicle_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前車両',
  `maker_id` int DEFAULT NULL COMMENT 'メーカーID',
  `store_id` int DEFAULT NULL COMMENT '売上ID'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `t_rental_orders`
--

CREATE TABLE `t_rental_orders` (
  `rental_orders_id` int NOT NULL COMMENT '発注明細ID:自動採番',
  `total_amount` float DEFAULT NULL COMMENT '合計',
  `payment_method_id` int DEFAULT NULL COMMENT '作成処理:プログラムで設定、API名、関数名',
  `rental_status` int DEFAULT NULL COMMENT '作成処理:プログラムで設定、API名、関数名',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時:プログラムでは設定しない',
  `created_by` int DEFAULT NULL COMMENT '作成処理:プログラムで設定、API名、関数名',
  `modified_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新日時:プログラムでは設定しない',
  `modified_by` int DEFAULT NULL COMMENT '更新処理:プログラムで設定、API名、関数名',
  `deleted_at` datetime DEFAULT NULL COMMENT '削除日時',
  `deleted_by` int DEFAULT NULL COMMENT '削除者',
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0' COMMENT '登録旗deleted: 0：消去未 ,1：消去済'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `t_rental_order_detail`
--

CREATE TABLE `t_rental_order_detail` (
  `rental_orders_detail_id` int NOT NULL COMMENT '発注明細ID:自動採番',
  `rental_order_id` int NOT NULL COMMENT '車両ID',
  `vehicle_id` int NOT NULL COMMENT '車両ID',
  `option_id` int NOT NULL COMMENT '車両ID',
  `quantity` int NOT NULL COMMENT '数量',
  `amount` float NOT NULL COMMENT '小計',
  `retal_start_date` datetime NOT NULL COMMENT 'レンタル開始日',
  `retal_end_date` datetime NOT NULL COMMENT 'レンタル終了日',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時:プログラムでは設定しない',
  `created_by` int DEFAULT NULL COMMENT '作成処理:プログラムで設定、API名、関数名',
  `modified_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新日時:プログラムでは設定しない',
  `modified_by` int DEFAULT NULL COMMENT '更新処理:プログラムで設定、API名、関数名',
  `deleted_at` datetime DEFAULT NULL COMMENT '削除日時',
  `deleted_by` int DEFAULT NULL COMMENT '削除者',
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0' COMMENT '登録旗deleted: 0：消去未 ,1：消去済'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `m_accounts`
--
ALTER TABLE `m_accounts`
  ADD PRIMARY KEY (`account_id`);

--
-- Indexes for table `m_account_base`
--
ALTER TABLE `m_account_base`
  ADD PRIMARY KEY (`account_base_id`),
  ADD KEY `base_id` (`base_id`),
  ADD KEY `modified_by` (`modified_by`),
  ADD KEY `deleted_by` (`deleted_by`),
  ADD KEY `account_id` (`account_id`),
  ADD KEY `created_by` (`created_by`);

--
-- Indexes for table `m_base`
--
ALTER TABLE `m_base`
  ADD PRIMARY KEY (`base_id`),
  ADD KEY `pref_code` (`pref_code`),
  ADD KEY `created_by` (`created_by`),
  ADD KEY `deleted_by` (`deleted_by`),
  ADD KEY `modified_by` (`modified_by`);

--
-- Indexes for table `m_insurances`
--
ALTER TABLE `m_insurances`
  ADD PRIMARY KEY (`insurance_id`);

--
-- Indexes for table `m_makers`
--
ALTER TABLE `m_makers`
  ADD PRIMARY KEY (`maker_id`);

--
-- Indexes for table `m_options`
--
ALTER TABLE `m_options`
  ADD PRIMARY KEY (`option_id`);

--
-- Indexes for table `m_payment_methods`
--
ALTER TABLE `m_payment_methods`
  ADD PRIMARY KEY (`payment_method_id`);

--
-- Indexes for table `m_prefecture`
--
ALTER TABLE `m_prefecture`
  ADD PRIMARY KEY (`pref_id`);

--
-- Indexes for table `m_stores`
--
ALTER TABLE `m_stores`
  ADD PRIMARY KEY (`store_id`);

--
-- Indexes for table `m_vehicles`
--
ALTER TABLE `m_vehicles`
  ADD PRIMARY KEY (`vehicle_id`),
  ADD KEY `maker_id` (`maker_id`),
  ADD KEY `store_id` (`store_id`);

--
-- Indexes for table `t_rental_orders`
--
ALTER TABLE `t_rental_orders`
  ADD PRIMARY KEY (`rental_orders_id`),
  ADD KEY `created_by` (`created_by`),
  ADD KEY `deleted_by` (`deleted_by`),
  ADD KEY `modified_by` (`modified_by`),
  ADD KEY `payment_method_id` (`payment_method_id`);

--
-- Indexes for table `t_rental_order_detail`
--
ALTER TABLE `t_rental_order_detail`
  ADD PRIMARY KEY (`rental_orders_detail_id`),
  ADD KEY `created_by` (`created_by`),
  ADD KEY `deleted_by` (`deleted_by`),
  ADD KEY `modified_by` (`modified_by`),
  ADD KEY `option_id` (`option_id`),
  ADD KEY `rental_order_id` (`rental_order_id`),
  ADD KEY `vehicle_id` (`vehicle_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `m_accounts`
--
ALTER TABLE `m_accounts`
  MODIFY `account_id` int NOT NULL AUTO_INCREMENT COMMENT 'アカウントID';

--
-- AUTO_INCREMENT for table `m_account_base`
--
ALTER TABLE `m_account_base`
  MODIFY `account_base_id` int NOT NULL AUTO_INCREMENT COMMENT 'アカウントベースID';

--
-- AUTO_INCREMENT for table `m_base`
--
ALTER TABLE `m_base`
  MODIFY `base_id` int NOT NULL AUTO_INCREMENT COMMENT '拠点ID';

--
-- AUTO_INCREMENT for table `m_insurances`
--
ALTER TABLE `m_insurances`
  MODIFY `insurance_id` int NOT NULL AUTO_INCREMENT COMMENT '保険ID';

--
-- AUTO_INCREMENT for table `m_makers`
--
ALTER TABLE `m_makers`
  MODIFY `maker_id` int NOT NULL AUTO_INCREMENT COMMENT 'メーカーID';

--
-- AUTO_INCREMENT for table `m_options`
--
ALTER TABLE `m_options`
  MODIFY `option_id` int NOT NULL AUTO_INCREMENT COMMENT 'オプションID';

--
-- AUTO_INCREMENT for table `m_payment_methods`
--
ALTER TABLE `m_payment_methods`
  MODIFY `payment_method_id` int NOT NULL AUTO_INCREMENT COMMENT '保険ID';

--
-- AUTO_INCREMENT for table `m_prefecture`
--
ALTER TABLE `m_prefecture`
  MODIFY `pref_id` int NOT NULL AUTO_INCREMENT COMMENT '県ID';

--
-- AUTO_INCREMENT for table `m_stores`
--
ALTER TABLE `m_stores`
  MODIFY `store_id` int NOT NULL AUTO_INCREMENT COMMENT '売上ID';

--
-- AUTO_INCREMENT for table `m_vehicles`
--
ALTER TABLE `m_vehicles`
  MODIFY `vehicle_id` int NOT NULL AUTO_INCREMENT COMMENT '車両ID';

--
-- AUTO_INCREMENT for table `t_rental_orders`
--
ALTER TABLE `t_rental_orders`
  MODIFY `rental_orders_id` int NOT NULL AUTO_INCREMENT COMMENT '発注明細ID:自動採番';

--
-- AUTO_INCREMENT for table `t_rental_order_detail`
--
ALTER TABLE `t_rental_order_detail`
  MODIFY `rental_orders_detail_id` int NOT NULL AUTO_INCREMENT COMMENT '発注明細ID:自動採番';

--
-- Constraints for dumped tables
--

--
-- Constraints for table `m_account_base`
--
ALTER TABLE `m_account_base`
  ADD CONSTRAINT `m_account_base_ibfk_2` FOREIGN KEY (`base_id`) REFERENCES `m_base` (`base_id`),
  ADD CONSTRAINT `m_account_base_ibfk_3` FOREIGN KEY (`modified_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `m_account_base_ibfk_4` FOREIGN KEY (`deleted_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `m_account_base_ibfk_5` FOREIGN KEY (`account_id`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `m_account_base_ibfk_6` FOREIGN KEY (`created_by`) REFERENCES `m_accounts` (`account_id`);

--
-- Constraints for table `m_base`
--
ALTER TABLE `m_base`
  ADD CONSTRAINT `m_base_ibfk_4` FOREIGN KEY (`pref_code`) REFERENCES `m_prefecture` (`pref_id`),
  ADD CONSTRAINT `m_base_ibfk_5` FOREIGN KEY (`created_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `m_base_ibfk_6` FOREIGN KEY (`deleted_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `m_base_ibfk_7` FOREIGN KEY (`modified_by`) REFERENCES `m_accounts` (`account_id`);

--
-- Constraints for table `m_vehicles`
--
ALTER TABLE `m_vehicles`
  ADD CONSTRAINT `m_vehicles_ibfk_1` FOREIGN KEY (`maker_id`) REFERENCES `m_makers` (`maker_id`),
  ADD CONSTRAINT `m_vehicles_ibfk_2` FOREIGN KEY (`store_id`) REFERENCES `m_stores` (`store_id`);

--
-- Constraints for table `t_rental_orders`
--
ALTER TABLE `t_rental_orders`
  ADD CONSTRAINT `t_rental_orders_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `t_rental_orders_ibfk_2` FOREIGN KEY (`deleted_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `t_rental_orders_ibfk_3` FOREIGN KEY (`modified_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `t_rental_orders_ibfk_4` FOREIGN KEY (`payment_method_id`) REFERENCES `m_payment_methods` (`payment_method_id`);

--
-- Constraints for table `t_rental_order_detail`
--
ALTER TABLE `t_rental_order_detail`
  ADD CONSTRAINT `t_rental_order_detail_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `t_rental_order_detail_ibfk_2` FOREIGN KEY (`deleted_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `t_rental_order_detail_ibfk_3` FOREIGN KEY (`modified_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `t_rental_order_detail_ibfk_4` FOREIGN KEY (`option_id`) REFERENCES `m_options` (`option_id`),
  ADD CONSTRAINT `t_rental_order_detail_ibfk_5` FOREIGN KEY (`rental_order_id`) REFERENCES `t_rental_orders` (`rental_orders_id`),
  ADD CONSTRAINT `t_rental_order_detail_ibfk_6` FOREIGN KEY (`vehicle_id`) REFERENCES `m_vehicles` (`vehicle_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
