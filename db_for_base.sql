-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: pclcm_mysql
-- Thời gian đã tạo: Th6 14, 2023 lúc 01:02 PM
-- Phiên bản máy phục vụ: 8.0.23
-- Phiên bản PHP: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `db_for_base`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('0ac9154ee0ec');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `m_accounts`
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

--
-- Đang đổ dữ liệu cho bảng `m_accounts`
--

INSERT INTO `m_accounts` (`account_id`, `account_cd`, `ext_account_id`, `account_name`, `email_address`, `account_status`, `is_system_manager`, `version`, `created_at`, `created_by`, `modified_at`, `modified_by`, `deleted_at`, `deleted_by`, `is_deleted`) VALUES
(1, 'KH00001', NULL, 'KH00001', 'kh00001@gmail.com', 0, 0, 1, '2023-06-13 13:03:03', NULL, '2023-06-13 13:03:03', NULL, NULL, NULL, 0),
(2, 'KH00002', NULL, 'KH00002', 'kh00002@gmail.com', 0, 0, 1, '2023-06-13 13:03:03', NULL, '2023-06-13 13:03:03', NULL, NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `m_account_base`
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
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `m_account_base`
--

INSERT INTO `m_account_base` (`account_base_id`, `account_id`, `base_id`, `version`, `created_at`, `created_by`, `modified_at`, `modified_by`, `deleted_at`, `deleted_by`, `is_deleted`) VALUES
(1, 1, 1, 1, '2023-06-13 13:07:46', NULL, '2023-06-13 13:07:46', NULL, NULL, NULL, 0),
(2, 1, 2, 1, '2023-06-13 13:07:46', NULL, '2023-06-13 13:07:46', NULL, NULL, NULL, 0),
(3, 2, 1, 1, '2023-06-13 13:07:46', NULL, '2023-06-13 13:07:46', NULL, NULL, NULL, 0),
(4, 2, 2, 1, '2023-06-13 13:07:46', NULL, '2023-06-13 13:07:46', NULL, NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `m_base`
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

--
-- Đang đổ dữ liệu cho bảng `m_base`
--

INSERT INTO `m_base` (`base_id`, `base_cd`, `base_name`, `zip_code`, `pref_code`, `address`, `addressee`, `telephone_number`, `fax_number`, `e_mail_address`, `note`, `version`, `created_at`, `created_by`, `modified_at`, `modified_by`, `deleted_at`, `deleted_by`, `is_deleted`) VALUES
(1, 'BC00001', 'BC00001', 'BC00001', 1, 'Hà Nội', 'Hà Nội', '+84 24 2525 2221', NULL, 'bc0001@gmail.com', NULL, 1, '2023-06-13 13:06:37', NULL, '2023-06-13 13:06:37', NULL, NULL, NULL, 0),
(2, 'BC00002', 'BC00002', 'BC00002', 2, 'Cần Thơ', 'Cần Thơ', '+84 24 2525 2221', NULL, 'bc0002@gmail.com', NULL, 1, '2023-06-13 13:06:37', NULL, '2023-06-13 13:06:37', NULL, NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `m_insurances`
--

CREATE TABLE `m_insurances` (
  `insurance_id` int NOT NULL COMMENT '保険ID',
  `insurance_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前保険',
  `insurance_value` float DEFAULT NULL COMMENT 'Giá bảo hiểm'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `m_insurances`
--

INSERT INTO `m_insurances` (`insurance_id`, `insurance_name`, `insurance_value`) VALUES
(4, 'insurance 2', 100000),
(5, 'insurance 243', 200000),
(6, 'insurance 60', 300000);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `m_makers`
--

CREATE TABLE `m_makers` (
  `maker_id` int NOT NULL COMMENT 'メーカーID',
  `maker_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前メーカー'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `m_makers`
--

INSERT INTO `m_makers` (`maker_id`, `maker_name`) VALUES
(1, 'maker 1'),
(2, 'maker 2'),
(3, 'maker 3'),
(4, 'maker 4'),
(5, 'maker 5');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `m_models`
--

CREATE TABLE `m_models` (
  `model_id` int NOT NULL COMMENT 'モデルID',
  `model_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前モデル'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `m_models`
--

INSERT INTO `m_models` (`model_id`, `model_name`) VALUES
(1, 'model 1'),
(2, 'model 2'),
(3, 'model 3'),
(4, 'model 4'),
(5, 'model 5');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `m_options`
--

CREATE TABLE `m_options` (
  `option_id` int NOT NULL COMMENT 'オプションID',
  `option_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前オプション',
  `option_value` float DEFAULT NULL COMMENT 'Giá option'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `m_options`
--

INSERT INTO `m_options` (`option_id`, `option_name`, `option_value`) VALUES
(5, 'option 1', 200000),
(6, 'option 2', 250000),
(7, 'option 3', 300000),
(8, 'option 4', 350000),
(9, 'option 5', 400000);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `m_payment_methods`
--

CREATE TABLE `m_payment_methods` (
  `payment_method_id` int NOT NULL COMMENT 'お支払い方法ID',
  `payment_method_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前お支払い方法'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `m_payment_methods`
--

INSERT INTO `m_payment_methods` (`payment_method_id`, `payment_method_name`) VALUES
(1, 'Thanh toán tiền mặt'),
(2, 'ATM nội địa'),
(3, 'Thẻ quốc tế');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `m_prefecture`
--

CREATE TABLE `m_prefecture` (
  `pref_id` int NOT NULL COMMENT '県ID',
  `pref_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前県'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `m_prefecture`
--

INSERT INTO `m_prefecture` (`pref_id`, `pref_name`) VALUES
(1, 'Hà Nội'),
(2, 'Cần Thơ '),
(3, 'Đà Nẵng'),
(4, 'Nha Trang'),
(5, 'Đà Lạc');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `m_stores`
--

CREATE TABLE `m_stores` (
  `store_id` int NOT NULL COMMENT '売上ID',
  `store_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前売上'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `m_stores`
--

INSERT INTO `m_stores` (`store_id`, `store_name`) VALUES
(1, 'store 1'),
(2, 'store 2'),
(3, 'store 3'),
(4, 'store 4'),
(5, 'store 5');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `m_vehicles`
--

CREATE TABLE `m_vehicles` (
  `vehicle_id` int NOT NULL COMMENT '車両ID',
  `vehicle_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '名前車両',
  `maker_id` int DEFAULT NULL COMMENT 'メーカーID',
  `store_id` int DEFAULT NULL COMMENT '売上ID',
  `year` int DEFAULT NULL COMMENT '製造年',
  `mileage` int DEFAULT NULL COMMENT '車の走行距離(km)',
  `vehicle_status` int DEFAULT NULL COMMENT '車の状態：1-利用可能、2-レンタル済、3-保守中',
  `vehicle_seat` int DEFAULT NULL COMMENT 'Số lượng ghế',
  `vehicle_type` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Kiểu xe',
  `vehicle_value` float DEFAULT NULL COMMENT 'Giá xe',
  `vehicleEngine` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Động cơ xe',
  `vehicleRating` varchar(5) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Xếp hạng',
  `vehicleConsumedEnergy` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Năng lượng tiêu hao trên 100km',
  `vehicle_describe` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Mô tả'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `m_vehicles`
--

INSERT INTO `m_vehicles` (`vehicle_id`, `vehicle_name`, `maker_id`, `store_id`, `year`, `mileage`, `vehicle_status`, `vehicle_seat`, `vehicle_type`, `vehicle_value`, `vehicleEngine`, `vehicleRating`, `vehicleConsumedEnergy`, `vehicle_describe`) VALUES
(1, 'Car 1', 1, 1, 2022, 1000, 0, 4, NULL, 1000000000, 'Số tự động', '5', NULL, 'xe siêu sang'),
(2, 'Car 2', 2, 2, 2022, 1000, 0, 7, NULL, 2000000000, 'Số tự động', '5', NULL, 'xe siêu sang');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `m_vehicle_img`
--

CREATE TABLE `m_vehicle_img` (
  `vehicleImageid` int NOT NULL,
  `vehicleId` int DEFAULT NULL,
  `image` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `m_vehicle_img`
--

INSERT INTO `m_vehicle_img` (`vehicleImageid`, `vehicleId`, `image`) VALUES
(1, 1, 'https://cdn.vuetifyjs.com/images/cards/halcyon.png'),
(2, 2, 'https://cdn.vuetifyjs.com/images/cards/halcyon.png');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `t_rental_orders`
--

CREATE TABLE `t_rental_orders` (
  `rental_orders_id` int NOT NULL COMMENT '発注明細ID:自動採番',
  `total_amount` float DEFAULT NULL COMMENT '合計',
  `payment_method_id` int DEFAULT NULL COMMENT 'お支払い方法ID',
  `rental_status` int DEFAULT NULL COMMENT '注文の状態。1:新規、2:確認中、3:確認済、4:支払い済み、5:キャンセル',
  `paymented_at` datetime NOT NULL COMMENT '支払日',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時:プログラムでは設定しない',
  `created_by` int DEFAULT NULL COMMENT '作成者',
  `modified_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新日時:プログラムでは設定しない',
  `modified_by` int DEFAULT NULL COMMENT '更新者',
  `deleted_at` datetime DEFAULT NULL COMMENT '削除日時',
  `deleted_by` int DEFAULT NULL COMMENT '削除者',
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0' COMMENT '登録旗deleted: 0：消去未 ,1：消去済'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `t_rental_orders`
--

INSERT INTO `t_rental_orders` (`rental_orders_id`, `total_amount`, `payment_method_id`, `rental_status`, `paymented_at`, `created_at`, `created_by`, `modified_at`, `modified_by`, `deleted_at`, `deleted_by`, `is_deleted`) VALUES
(2, 2, 1, 1, '2023-06-16 00:00:00', '2023-06-14 21:33:39', NULL, '2023-06-14 21:33:39', NULL, NULL, NULL, 0),
(3, 1, 1, 1, '2023-06-16 00:00:00', '2023-06-14 21:35:18', NULL, '2023-06-14 21:35:18', NULL, NULL, NULL, 0),
(4, 2525250, 1, 1, '2023-06-16 00:00:00', '2023-06-14 21:37:00', NULL, '2023-06-14 21:37:00', NULL, NULL, NULL, 0),
(5, 1, 1, 1, '2023-06-16 00:00:00', '2023-06-14 21:43:50', NULL, '2023-06-14 21:43:50', NULL, NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `t_rental_order_detail`
--

CREATE TABLE `t_rental_order_detail` (
  `rental_orders_detail_id` int NOT NULL COMMENT '発注明細ID:自動採番',
  `rental_order_id` int NOT NULL COMMENT '車両ID',
  `vehicle_id` int NOT NULL COMMENT '車両ID',
  `option_id` int NOT NULL COMMENT '車両ID',
  `quantity` int NOT NULL COMMENT '数量',
  `amount` float NOT NULL COMMENT '小計',
  `rental_start_date` datetime NOT NULL COMMENT 'レンタル開始日',
  `rental_end_date` datetime NOT NULL COMMENT 'レンタル終了日',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時:プログラムでは設定しない',
  `created_by` int DEFAULT NULL COMMENT '作成者',
  `modified_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新日時:プログラムでは設定しない',
  `modified_by` int DEFAULT NULL COMMENT '更新者',
  `deleted_at` datetime DEFAULT NULL COMMENT '削除日時',
  `deleted_by` int DEFAULT NULL COMMENT '削除者',
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0' COMMENT '登録旗deleted: 0：消去未 ,1：消去済'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `t_rental_order_detail`
--

INSERT INTO `t_rental_order_detail` (`rental_orders_detail_id`, `rental_order_id`, `vehicle_id`, `option_id`, `quantity`, `amount`, `rental_start_date`, `rental_end_date`, `created_at`, `created_by`, `modified_at`, `modified_by`, `deleted_at`, `deleted_by`, `is_deleted`) VALUES
(2, 2, 1, 5, 4, 1, '2023-06-16 00:00:00', '2023-06-18 00:00:00', '2023-06-14 21:33:39', NULL, '2023-06-14 21:33:39', NULL, NULL, NULL, 0),
(3, 3, 1, 5, 4, 1, '2023-06-16 00:00:00', '2023-06-18 00:00:00', '2023-06-14 21:35:18', NULL, '2023-06-14 21:35:18', NULL, NULL, NULL, 0),
(4, 4, 1, 5, 4, 1, '2023-06-16 00:00:00', '2023-06-18 00:00:00', '2023-06-14 21:37:00', NULL, '2023-06-14 21:37:00', NULL, NULL, NULL, 0),
(5, 5, 1, 5, 4, 1, '2023-06-16 00:00:00', '2023-06-18 00:00:00', '2023-06-14 21:43:50', NULL, '2023-06-14 21:43:50', NULL, NULL, NULL, 0);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Chỉ mục cho bảng `m_accounts`
--
ALTER TABLE `m_accounts`
  ADD PRIMARY KEY (`account_id`);

--
-- Chỉ mục cho bảng `m_account_base`
--
ALTER TABLE `m_account_base`
  ADD PRIMARY KEY (`account_base_id`),
  ADD KEY `account_id` (`account_id`),
  ADD KEY `base_id` (`base_id`),
  ADD KEY `created_by` (`created_by`),
  ADD KEY `deleted_by` (`deleted_by`),
  ADD KEY `modified_by` (`modified_by`);

--
-- Chỉ mục cho bảng `m_base`
--
ALTER TABLE `m_base`
  ADD PRIMARY KEY (`base_id`),
  ADD KEY `created_by` (`created_by`),
  ADD KEY `deleted_by` (`deleted_by`),
  ADD KEY `modified_by` (`modified_by`),
  ADD KEY `pref_code` (`pref_code`);

--
-- Chỉ mục cho bảng `m_insurances`
--
ALTER TABLE `m_insurances`
  ADD PRIMARY KEY (`insurance_id`);

--
-- Chỉ mục cho bảng `m_makers`
--
ALTER TABLE `m_makers`
  ADD PRIMARY KEY (`maker_id`);

--
-- Chỉ mục cho bảng `m_models`
--
ALTER TABLE `m_models`
  ADD PRIMARY KEY (`model_id`);

--
-- Chỉ mục cho bảng `m_options`
--
ALTER TABLE `m_options`
  ADD PRIMARY KEY (`option_id`);

--
-- Chỉ mục cho bảng `m_payment_methods`
--
ALTER TABLE `m_payment_methods`
  ADD PRIMARY KEY (`payment_method_id`);

--
-- Chỉ mục cho bảng `m_prefecture`
--
ALTER TABLE `m_prefecture`
  ADD PRIMARY KEY (`pref_id`);

--
-- Chỉ mục cho bảng `m_stores`
--
ALTER TABLE `m_stores`
  ADD PRIMARY KEY (`store_id`);

--
-- Chỉ mục cho bảng `m_vehicles`
--
ALTER TABLE `m_vehicles`
  ADD PRIMARY KEY (`vehicle_id`),
  ADD KEY `maker_id` (`maker_id`),
  ADD KEY `store_id` (`store_id`);

--
-- Chỉ mục cho bảng `m_vehicle_img`
--
ALTER TABLE `m_vehicle_img`
  ADD PRIMARY KEY (`vehicleImageid`),
  ADD KEY `vehicleId` (`vehicleId`);

--
-- Chỉ mục cho bảng `t_rental_orders`
--
ALTER TABLE `t_rental_orders`
  ADD PRIMARY KEY (`rental_orders_id`),
  ADD KEY `created_by` (`created_by`),
  ADD KEY `deleted_by` (`deleted_by`),
  ADD KEY `modified_by` (`modified_by`),
  ADD KEY `payment_method_id` (`payment_method_id`);

--
-- Chỉ mục cho bảng `t_rental_order_detail`
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
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `m_accounts`
--
ALTER TABLE `m_accounts`
  MODIFY `account_id` int NOT NULL AUTO_INCREMENT COMMENT 'アカウントID', AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `m_account_base`
--
ALTER TABLE `m_account_base`
  MODIFY `account_base_id` int NOT NULL AUTO_INCREMENT COMMENT 'アカウントベースID', AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT cho bảng `m_base`
--
ALTER TABLE `m_base`
  MODIFY `base_id` int NOT NULL AUTO_INCREMENT COMMENT '拠点ID', AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `m_insurances`
--
ALTER TABLE `m_insurances`
  MODIFY `insurance_id` int NOT NULL AUTO_INCREMENT COMMENT '保険ID', AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT cho bảng `m_makers`
--
ALTER TABLE `m_makers`
  MODIFY `maker_id` int NOT NULL AUTO_INCREMENT COMMENT 'メーカーID', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT cho bảng `m_models`
--
ALTER TABLE `m_models`
  MODIFY `model_id` int NOT NULL AUTO_INCREMENT COMMENT 'モデルID', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT cho bảng `m_options`
--
ALTER TABLE `m_options`
  MODIFY `option_id` int NOT NULL AUTO_INCREMENT COMMENT 'オプションID', AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT cho bảng `m_payment_methods`
--
ALTER TABLE `m_payment_methods`
  MODIFY `payment_method_id` int NOT NULL AUTO_INCREMENT COMMENT 'お支払い方法ID', AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT cho bảng `m_prefecture`
--
ALTER TABLE `m_prefecture`
  MODIFY `pref_id` int NOT NULL AUTO_INCREMENT COMMENT '県ID', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT cho bảng `m_stores`
--
ALTER TABLE `m_stores`
  MODIFY `store_id` int NOT NULL AUTO_INCREMENT COMMENT '売上ID', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT cho bảng `m_vehicles`
--
ALTER TABLE `m_vehicles`
  MODIFY `vehicle_id` int NOT NULL AUTO_INCREMENT COMMENT '車両ID', AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `m_vehicle_img`
--
ALTER TABLE `m_vehicle_img`
  MODIFY `vehicleImageid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `t_rental_orders`
--
ALTER TABLE `t_rental_orders`
  MODIFY `rental_orders_id` int NOT NULL AUTO_INCREMENT COMMENT '発注明細ID:自動採番', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT cho bảng `t_rental_order_detail`
--
ALTER TABLE `t_rental_order_detail`
  MODIFY `rental_orders_detail_id` int NOT NULL AUTO_INCREMENT COMMENT '発注明細ID:自動採番', AUTO_INCREMENT=6;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `m_account_base`
--
ALTER TABLE `m_account_base`
  ADD CONSTRAINT `m_account_base_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `m_account_base_ibfk_2` FOREIGN KEY (`base_id`) REFERENCES `m_base` (`base_id`),
  ADD CONSTRAINT `m_account_base_ibfk_3` FOREIGN KEY (`created_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `m_account_base_ibfk_4` FOREIGN KEY (`deleted_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `m_account_base_ibfk_5` FOREIGN KEY (`modified_by`) REFERENCES `m_accounts` (`account_id`);

--
-- Các ràng buộc cho bảng `m_base`
--
ALTER TABLE `m_base`
  ADD CONSTRAINT `m_base_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `m_base_ibfk_2` FOREIGN KEY (`deleted_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `m_base_ibfk_3` FOREIGN KEY (`modified_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `m_base_ibfk_4` FOREIGN KEY (`pref_code`) REFERENCES `m_prefecture` (`pref_id`);

--
-- Các ràng buộc cho bảng `m_vehicles`
--
ALTER TABLE `m_vehicles`
  ADD CONSTRAINT `m_vehicles_ibfk_1` FOREIGN KEY (`maker_id`) REFERENCES `m_makers` (`maker_id`),
  ADD CONSTRAINT `m_vehicles_ibfk_3` FOREIGN KEY (`store_id`) REFERENCES `m_stores` (`store_id`);

--
-- Các ràng buộc cho bảng `m_vehicle_img`
--
ALTER TABLE `m_vehicle_img`
  ADD CONSTRAINT `m_vehicle_img_ibfk_1` FOREIGN KEY (`vehicleId`) REFERENCES `m_vehicles` (`vehicle_id`);

--
-- Các ràng buộc cho bảng `t_rental_orders`
--
ALTER TABLE `t_rental_orders`
  ADD CONSTRAINT `t_rental_orders_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `t_rental_orders_ibfk_2` FOREIGN KEY (`deleted_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `t_rental_orders_ibfk_3` FOREIGN KEY (`modified_by`) REFERENCES `m_accounts` (`account_id`),
  ADD CONSTRAINT `t_rental_orders_ibfk_4` FOREIGN KEY (`payment_method_id`) REFERENCES `m_payment_methods` (`payment_method_id`);

--
-- Các ràng buộc cho bảng `t_rental_order_detail`
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
