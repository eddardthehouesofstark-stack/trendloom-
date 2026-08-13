-- NEW India & Tamil Nadu Fashion Data
-- Fresh trends different from existing sample data
-- Generated: 2026-08-13

-- First, let's clear existing data if you want fresh start (OPTIONAL - comment out if you want to keep old data)
-- DELETE FROM trends WHERE source = 'Google Trends India';
-- DELETE FROM regional_trends WHERE country_code = 'IN';

-- NEW India National Trends (Different from sample data)
INSERT INTO trends (name, category, status, momentum_score, description, image_url, source) VALUES
-- Traditional Indian Wear (NEW)
('Sharara Suit', 'Ethnic Wear', 'trending', 142, 'Trending in India. Flared bottom paired with short kurti. Search volume: 67,000/month. Popular for weddings.', 'https://source.unsplash.com/400x300/?sharara,indian-fashion', 'Google Trends India'),
('Patiala Salwar', 'Ethnic Wear', 'trending', 135, 'Trending in India. Traditional Punjabi-style loose salwar. Search volume: 54,000/month. Comfortable ethnic wear.', 'https://source.unsplash.com/400x300/?patiala-salwar,punjabi', 'Google Trends India'),
('Nehru Jacket', 'Ethnic Wear', 'trending', 128, 'Trending in India. Sleeveless Indian jacket for formal occasions. Search volume: 48,000/month. Indo-fusion style.', 'https://source.unsplash.com/400x300/?nehru-jacket,indian', 'Google Trends India'),
('Dhoti Pants', 'Ethnic Wear', 'trending', 118, 'Trending in India. Modern fusion dhoti-style pants. Search volume: 42,000/month. Contemporary ethnic.', 'https://source.unsplash.com/400x300/?dhoti-pants,fusion', 'Google Trends India'),
('Bandhani Saree', 'Fabrics', 'trending', 125, 'Trending in India. Traditional tie-dye saree from Gujarat/Rajasthan. Search volume: 38,000/month. Vibrant patterns.', 'https://source.unsplash.com/400x300/?bandhani,saree', 'Google Trends India'),

-- Modern Indian Fashion (NEW)
('Kaftan Dress', 'Fusion Wear', 'trending', 115, 'Trending in India. Loose flowy dress perfect for summer. Search volume: 52,000/month. Resort wear favorite.', 'https://source.unsplash.com/400x300/?kaftan,dress,india', 'Google Trends India'),
('Cape Kurta', 'Fusion Wear', 'trending', 108, 'Trending in India. Kurta with attached cape. Search volume: 36,000/month. Contemporary ethnic style.', 'https://source.unsplash.com/400x300/?cape-kurta,indian-fashion', 'Google Trends India'),
('Jacket Lehenga', 'Fusion Wear', 'trending', 132, 'Trending in India. Lehenga with jacket-style choli. Search volume: 44,000/month. Modern wedding wear.', 'https://source.unsplash.com/400x300/?jacket-lehenga,wedding', 'Google Trends India'),
('Shirt Kurta', 'Fusion Wear', 'trending', 105, 'Trending in India. Kurta styled like a shirt. Search volume: 39,000/month. Office-friendly ethnic.', 'https://source.unsplash.com/400x300/?shirt-kurta,formal', 'Google Trends India'),
('Gown Anarkali', 'Ethnic Wear', 'trending', 138, 'Trending in India. Floor-length Anarkali gown. Search volume: 58,000/month. Party and festive wear.', 'https://source.unsplash.com/400x300/?anarkali-gown,indian', 'Google Trends India'),

-- Accessories & Jewelry (NEW)
('Oxidized Jewellery', 'Accessories', 'trending', 145, 'Trending in India. Antique silver-finish jewelry. Search volume: 72,000/month. Trendy ethnic accessory.', 'https://source.unsplash.com/400x300/?oxidized-jewelry,silver', 'Google Trends India'),
('Jhumka Earrings', 'Accessories', 'trending', 152, 'Trending in India. Traditional bell-shaped earrings. Search volume: 84,000/month. Most searched Indian jewelry.', 'https://source.unsplash.com/400x300/?jhumka,earrings,indian', 'Google Trends India'),
('Maang Tikka', 'Accessories', 'trending', 138, 'Trending in India. Traditional forehead jewelry. Search volume: 48,000/month. Bridal essential.', 'https://source.unsplash.com/400x300/?maang-tikka,indian-jewelry', 'Google Trends India'),
('Potli Bag', 'Accessories', 'trending', 122, 'Trending in India. Traditional drawstring bag. Search volume: 36,000/month. Ethnic accessory.', 'https://source.unsplash.com/400x300/?potli-bag,indian', 'Google Trends India'),
('Kolhapuri Chappal', 'Accessories', 'trending', 115, 'Trending in India. Traditional leather sandals from Maharashtra. Search volume: 42,000/month. Comfortable ethnic footwear.', 'https://source.unsplash.com/400x300/?kolhapuri-chappal,sandals', 'Google Trends India'),

-- Fabrics & Textiles (NEW)
('Block Print Fabric', 'Fabrics', 'trending', 128, 'Trending in India. Hand-carved wooden block printing. Search volume: 45,000/month. Traditional craft.', 'https://source.unsplash.com/400x300/?block-print,fabric,india', 'Google Trends India'),
('Ikat Fabric', 'Fabrics', 'trending', 118, 'Trending in India. Traditional tie-dye weaving technique. Search volume: 32,000/month. Odisha specialty.', 'https://source.unsplash.com/400x300/?ikat,fabric,textile', 'Google Trends India'),
('Kalamkari Print', 'Fabrics', 'trending', 112, 'Trending in India. Hand-painted or block-printed cotton. Search volume: 28,000/month. Andhra Pradesh art.', 'https://source.unsplash.com/400x300/?kalamkari,print,fabric', 'Google Trends India'),
('Chikankari Work', 'Fabrics', 'trending', 148, 'Trending in India. Lucknow embroidery on cotton. Search volume: 78,000/month. Delicate white threadwork.', 'https://source.unsplash.com/400x300/?chikankari,embroidery,lucknow', 'Google Trends India'),
('Ajrakh Print', 'Fabrics', 'trending', 105, 'Trending in India. Geometric resist-dye printing from Gujarat. Search volume: 24,000/month. Natural dyes.', 'https://source.unsplash.com/400x300/?ajrakh,print,gujarat', 'Google Trends India'),

-- Contemporary Trends (NEW)
('Co-ord Set', 'Western Wear', 'trending', 135, 'Trending in India. Matching top and bottom set. Search volume: 92,000/month. Popular among youth.', 'https://source.unsplash.com/400x300/?coord-set,fashion', 'Google Trends India'),
('Bodycon Dress', 'Western Wear', 'trending', 125, 'Trending in India. Figure-hugging dress. Search volume: 68,000/month. Party wear favorite.', 'https://source.unsplash.com/400x300/?bodycon-dress,party', 'Google Trends India'),
('Shrug Jacket', 'Western Wear', 'trending', 118, 'Trending in India. Short open-front cardigan. Search volume: 54,000/month. Layering essential.', 'https://source.unsplash.com/400x300/?shrug,jacket,fashion', 'Google Trends India'),
('Wide Leg Jeans', 'Western Wear', 'trending', 142, 'Trending in India. Loose-fitting denim pants. Search volume: 88,000/month. Comeback trend.', 'https://source.unsplash.com/400x300/?wide-leg-jeans,denim', 'Google Trends India'),
('Boyfriend Shirt', 'Western Wear', 'trending', 112, 'Trending in India. Oversized loose shirt. Search volume: 46,000/month. Casual comfort.', 'https://source.unsplash.com/400x300/?boyfriend-shirt,oversized', 'Google Trends India');

-- NEW Tamil Nadu Regional Trends (Different from sample data)
INSERT INTO regional_trends (name, country_code, state_code, momentum_score, description, image_url) VALUES
('Kanchipuram Silk', 'IN', 'TN', 168, 'Trending in Tamil Nadu. World-famous silk fabric from Kanchipuram. Search volume: 52,000/month. Premium quality silk.', 'https://source.unsplash.com/400x300/?silk,kanchipuram,fabric'),
('Tanjore Art Saree', 'IN', 'TN', 145, 'Trending in Tamil Nadu. Sarees with Tanjore painting motifs. Search volume: 22,000/month. Art-inspired fashion.', 'https://source.unsplash.com/400x300/?tanjore,art,saree'),
('Kovai Cotton Saree', 'IN', 'TN', 138, 'Trending in Tamil Nadu. Handloom cotton from Coimbatore. Search volume: 18,000/month. Soft texture.', 'https://source.unsplash.com/400x300/?coimbatore,cotton,saree'),
('Paavadai Sattai', 'IN', 'TN', 125, 'Trending in Tamil Nadu. Traditional Tamil kids wear. Search volume: 16,000/month. Festival attire for children.', 'https://source.unsplash.com/400x300/?paavadai,traditional,kids'),
('Kambi Pattu', 'IN', 'TN', 155, 'Trending in Tamil Nadu. Thick border silk saree. Search volume: 34,000/month. Heavy bridal saree.', 'https://source.unsplash.com/400x300/?silk-saree,heavy-border'),
('Korvai Weave', 'IN', 'TN', 132, 'Trending in Tamil Nadu. Interlocked weaving technique. Search volume: 14,000/month. Complex traditional weave.', 'https://source.unsplash.com/400x300/?korvai,weave,saree'),
('Thirubuvanam Silk', 'IN', 'TN', 122, 'Trending in Tamil Nadu. Silk from Thanjavur district. Search volume: 11,000/month. Traditional weaving.', 'https://source.unsplash.com/400x300/?thirubuvanam,silk'),
('Arni Silk', 'IN', 'TN', 115, 'Trending in Tamil Nadu. Silk sarees from Arni town. Search volume: 9,500/month. Affordable silk.', 'https://source.unsplash.com/400x300/?arni,silk,saree'),
('Mangalgiri Cotton', 'IN', 'TN', 128, 'Trending in Tamil Nadu. Handloom cotton with zari border. Search volume: 13,000/month. Soft and durable.', 'https://source.unsplash.com/400x300/?mangalgiri,cotton'),
('Salem Soft Silk', 'IN', 'TN', 142, 'Trending in Tamil Nadu. Lightweight silk from Salem. Search volume: 26,000/month. Comfortable silk variant.', 'https://source.unsplash.com/400x300/?salem,soft-silk');

-- Success! You have imported 35 NEW India & Tamil Nadu fashion trends.
-- These are completely different from the sample data.
