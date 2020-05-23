#!/usr/bin/env python

#############################################################################
#																			#
# Copyright (c) 2020 Saeid Hosseinipoor <https://saeid-h.github.io/>		#
# All rights reserved.														#
# Licensed under the MIT License											#
#																			#
############################################################################# 

from __future__ import absolute_import, division, print_function

from PIL import Image 
import matplotlib.pyplot as plt
import os

import cv_io.sintel_io as sintel_io
import cv_io.flowlib as flowlib
import cv_io.pfmutil as pfmutil

NORMAL_IMAGE_FORMATS = ['png', 'pgm', 'jpg', 'jpeg', 'pmg']
IMAGE_TYPES = ['kitti-disparity', 'optical-flow', 'disparity', 'depth', 'file-extension-default']
IMAGE_TYPES_ERR_MSG = "ERROR: The image type is not supported. It should be one of ".format(IMAGE_TYPES)


# Auxiliary methods
def write_image(file_name, image):
	"""
	Save normal image of any format
	:param file_name: path and name of the image file to save
	:param image: image array
	:return: None
	"""
	return Image.fromarray(image).save(file_name)


# Methods from pfmutil:
read_pfm = lambda file_name: pfmutil.load(file_name)[0]
save_pfm = pfmutil.save 
show_pfm = pfmutil.show
pfm_scale  = lambda file_name: pfmutil.load(file_name)[1]


# Methods from flowlib:
read_flo = flowlib.read_flow
read_flo_png = flowlib.read_flow_png
save_flo = lambda file_name, flow: flowlib.write_flow(flow, file_name)
read_flo_seg = flowlib.segment_flow
flow_to_image = flowlib.flow_to_image
show_flow_from_file = flowlib.show_flow
show_flow = flowlib.visualize_flow
read_disp_asflow = flowlib.read_disp_png
save_disp_asflow = lambda file_name, disp: flowlib.disp_to_flowfile (disp, file_name)
warp_flow = flowlib.warp_image
scale_image = flowlib.scale_image


# Methods from sintel_io:
read_cam = sintel_io.cam_read
save_cam = sintel_io.cam_write
read_disp_sintel = sintel_io.disparity_read
save_disp_sintel = sintel_io.disparity_write
read_dpt = sintel_io.depth_read
save_dpt = sintel_io.depth_write
read_seg_sintel = sintel_io.segmentation_read
save_seg_sintel = sintel_io.segmentation_write
read_flow_sintel = sintel_io.flow_read
save_flow_sintel = sintel_io.flow_write


# General Modules
read_png = flowlib.read_image
save_png = write_image 
read_jpg = flowlib.read_image
save_jpg = write_image


def read(file_name, image_type='file-extension-default'):
	'''
	Read image
	:param file_name:
		File name and path in the disk that function loads from.
	:param image_type:
		The type of image as: 
			'kitti-disparity', 'optical-flow', 'disparity', 'file-extension-default'
	:return: image array
	'''
	
	ext = os.path.splitext(file_name)[1].lower()[1:]
	image_type = image_type.lower()
	if not image_type in IMAGE_TYPES:
		prtint (IMAGE_TYPES_ERR_MSG)
		return

	if image_type == 'file-extension-default':
		if ext in NORMAL_IMAGE_FORMATS:
			return flowlib.read_image(file_name)
		elif ext in ['flo']:
			return read_flo(file_name)
		elif ext in ['dpt']:
			return read_dpt(file_name)
		elif ext in ['pfm']:
			return read_pfm(file_name)
		else:
			print ("ERROR: The image type is unknown.")
	elif image_type == 'optical-flow':
		return read_flo(file_name)
	elif image_type == 'disparity':
		return read_pfm(file_name)
	elif image_type == 'depth':
		return read_dpt(file_name)
	elif image_type == 'kitti-disparity':
		return flowlib.read_image(file_name).astype(np.float32) / 256.
	else:
		print ("This image type is not implemented.")


def save(file_name, image, image_type='file-extension-default'):
	'''
	Save image
	:param file_name:
		File name and path in the disk that function save to.
	:param image:
		The image array that will be saved on disl as file_name.
	:param image_type:
		The type of image as: 
			'kitti-disparity', 'optical-flow', 'disparity', 'file-extension-default'
	:return: None
	'''

	ext = os.path.splitext(file_name)[1].lower()[1:]
	image_type = image_type.lower()
	if not image_type in IMAGE_TYPES:
		prtint (IMAGE_TYPES_ERR_MSG)
		return

	if image_type == 'file-extension-default':
		if ext in NORMAL_IMAGE_FORMATS:
			return write_image(file_name, image)
		elif ext in ['flo']:
			return save_flo(file_name, image)
		elif ext in ['dpt']:
			return save_dpt(file_name, image)
		elif ext in ['pfm']:
			return save_pfm(file_name, image)
		else:
			print ("ERROR: The image type is unknown.") 
	elif image_type == 'optical-flow':
		if len(image.shape) == 3 and image.shape[2] == 2:
			return save_flo(file_name, image.astype(np.float32))
		else:
			print ("ERROR: The image type is unknown.")
	elif image_type == 'disparity':
		return save_pfm(file_name, image)
	elif image_type == 'depth':
		return save_dpt(file_name, image)
	elif image_type == 'kitti-disparity':
		return write_image(file_name, (image*256.).astype(np.uint16))
	else:
		print ("This image type is not implemented.")


def show(parameter):
	'''
	Show image
	:param parameter:
		If it's a string (filename), it reads the image from file and shows it.
		If it is a image array it shows it
	:return: None
	'''
	image = read(parameter) if parameter is str else parameter
	if len(parameter.shape == 3) and parameter.shape[-1] == 2:
		show_flow(parameter)
	else: 
		if len(parameter.shape == 3) and parameter.shape[-1] == 1:
			parameter = np.squeeze(parameter)
			plt.imshow(parameter.astype(np.float32), cmap='gray')
		else:
			plt.imshow(parameter.astype(np.float32))
		plt.show()

	

if __name__ == "__main__":
	pass