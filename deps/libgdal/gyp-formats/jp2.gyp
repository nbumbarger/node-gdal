{
	"includes": [
		"../common.gypi"
	],
	"targets": [
		{
			"target_name": "libgdal_jp2_frmt",
			"type": "static_library",
			"sources": [
			    "../gdal/frmts/jpeg2000/jpeg2000dataset.cpp",
				"../gdal/frmts/jpeg2000/jpeg2000_vsil_io.cpp",
				"../gdal/frmts/jpeg2000/jpeg2000_vsil_io.h"
			],
			"include_dirs": [
				"../gdal/frmts/jpeg2000"
			]
		}
	]
}
