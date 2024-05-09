-- list bands with glam rock as their main style ordered by their longevity
SELECT band_name, IFNULL (split, 2022) - formed as lifespan
	FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
