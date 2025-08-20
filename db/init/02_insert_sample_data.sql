-- Wstawianie przykładowych danych - Gaming E-commerce

-- Kategorie
INSERT INTO categories (name, description, slug) VALUES 
    ('Keyboards', 'Mechanical and gaming keyboards', 'keyboards'),
    ('Mice', 'Gaming mice and mousepads', 'mice'),
    ('Headsets', 'Gaming headphones and headsets', 'headsets'),
    ('Monitors', 'Gaming monitors and displays', 'monitors'),
    ('Graphics Cards', 'Gaming graphics cards and GPUs', 'graphics-cards'),
    ('Accessories', 'Gaming accessories and peripherals', 'accessories')
ON CONFLICT (name) DO NOTHING;

-- Produkty Gaming
INSERT INTO products (name, description, price, category_id, sku, brand, stock_quantity, image_url) VALUES 
    -- Klawiatury
    ('HyperX Alloy Elite RGB', 'Mechanical gaming keyboard with Cherry MX switches and RGB lighting', 299.99, 1, 'HX-KB-AE-RGB', 'HyperX', 15, '/images/hyperx-alloy-elite.jpg'),
    ('Corsair K95 RGB Platinum', 'Premium mechanical gaming keyboard with macro keys', 459.99, 1, 'COR-K95-RGB', 'Corsair', 8, '/images/corsair-k95.jpg'),
    ('Razer BlackWidow V3 Pro', 'Wireless mechanical gaming keyboard', 399.99, 1, 'RZ-BW-V3-PRO', 'Razer', 12, '/images/razer-blackwidow.jpg'),
    
    -- Myszki
    ('Logitech G Pro X Superlight', 'Ultra-lightweight wireless gaming mouse', 329.99, 2, 'LOG-GPRO-SL', 'Logitech', 25, '/images/logitech-gpro.jpg'),
    ('Razer DeathAdder V3', 'Ergonomic gaming mouse with high precision sensor', 179.99, 2, 'RZ-DA-V3', 'Razer', 30, '/images/razer-deathadder.jpg'),
    ('SteelSeries Rival 650', 'Wireless gaming mouse with customizable weight', 249.99, 2, 'SS-RIV-650', 'SteelSeries', 18, '/images/steelseries-rival.jpg'),
    
    -- Słuchawki
    ('SteelSeries Arctis 7P', 'Wireless gaming headset for PlayStation', 389.99, 3, 'SS-ARC-7P', 'SteelSeries', 20, '/images/steelseries-arctis7p.jpg'),
    ('HyperX Cloud Alpha', 'Gaming headset with dual chamber drivers', 199.99, 3, 'HX-CA-ALPHA', 'HyperX', 35, '/images/hyperx-cloud-alpha.jpg'),
    ('Corsair Virtuoso RGB', 'High-fidelity gaming headset', 449.99, 3, 'COR-VIRT-RGB', 'Corsair', 14, '/images/corsair-virtuoso.jpg'),
    
    -- Monitory
    ('ASUS ROG Swift PG259QN', '360Hz gaming monitor 24.5 inch', 1299.99, 4, 'ASUS-PG259QN', 'ASUS', 5, '/images/asus-pg259qn.jpg'),
    ('MSI Optix MAG274QRF-QD', '165Hz QHD gaming monitor', 899.99, 4, 'MSI-MAG274', 'MSI', 8, '/images/msi-optix-mag274.jpg'),
    ('Samsung Odyssey G7', 'Curved 240Hz gaming monitor', 1199.99, 4, 'SAM-ODY-G7', 'Samsung', 6, '/images/samsung-odyssey-g7.jpg'),
    
    -- Karty graficzne
    ('NVIDIA RTX 4080 SUPER', 'High-end gaming graphics card', 4299.99, 5, 'NV-RTX4080S', 'NVIDIA', 3, '/images/rtx-4080-super.jpg'),
    ('AMD Radeon RX 7900 XTX', 'High-performance gaming GPU', 3899.99, 5, 'AMD-RX7900XTX', 'AMD', 4, '/images/amd-rx7900xtx.jpg'),
    ('RTX 4070 Ti SUPER', 'Mid-range gaming graphics card', 2999.99, 5, 'NV-RTX4070TIS', 'NVIDIA', 7, '/images/rtx-4070ti-super.jpg'),
    
    -- Akcesoria
    ('Corsair MM300 Extended', 'Large gaming mousepad', 79.99, 6, 'COR-MM300-EXT', 'Corsair', 45, '/images/corsair-mm300.jpg'),
    ('Razer Base Station V2', 'RGB headset stand with USB hub', 149.99, 6, 'RZ-BASE-V2', 'Razer', 22, '/images/razer-base-station.jpg'),
    ('HyperX QuadCast S', 'RGB USB condenser microphone', 399.99, 6, 'HX-QC-S', 'HyperX', 16, '/images/hyperx-quadcast-s.jpg');
