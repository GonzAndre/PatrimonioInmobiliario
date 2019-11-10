#!/usr/bin/env python
# -*- coding: utf-8 -*-

PROPERTY_USE_CHOICE = (
    ('IGL', 'Iglesia'),
    ('GRU', 'Grupo'),
    ('COL', 'Colegio'),
    ('HAB', 'Habitacional'),
    ('Otro', 'Otro')
)

WRITING_DATA_CHOICE = (
    ('COM', 'Compraventa'),
    ('DON', 'Donación'),
    ('SUB','Subdivisión'),
    ('Otro', 'Otro')
)

REGION_CHOICE = (
    ('RM', 'Region Metropolitana'),
    ('TP', 'Region de Tarapaca'),
    ('AF', 'Region de Antofagasta'),
    ('CQ', 'Region de Coquimbo'),
    ('VP', 'Region de Valparaiso'),
    ('BO', "Region de O'Higgins"),
    ('ML', 'Region del Maule'),
    ('CP', 'Region de Concepcion'),
    ('AR', 'Region de la Araucania'),
    ('LG', 'Region de los lagos'),
    ('AS', 'Region de Aysen'),
    ('MG', 'Region de Magallanes'),
    ('RS', 'Region de los Rios'),
    ('AP', 'Region de Arica y Parinacota'),
    ('ÑB', 'Region del Ñuble')
)

ATTRIBUTES_CHOICE = (
    ('TC', 'Tipo contrato'),
    ('ES', 'Escritura'),
    ('DC', 'Certificado de dominio'),
    ('PR', 'Prohibiciones'),
    ('SE', 'Expropiación SERVIU'),
    ('OT', 'Otro'),
    ('EM', 'Expropiación Municipalidad'),
    ('CP', 'CIP'),
    ('NC', 'Número certificado'),
    ('PL', 'Planos'),
    ('PE', 'Permiso de edificación'),
    ('RM', 'Recepción municipal'),
    ('CA', 'Certificado avalúo'),
    ('CD', 'Certificado no deuda')
)

POSITION_CHOICE = (
    ('DIG', 'Digitador'),
    ('ADM', 'Administrador'),
    ('VIS', 'Visualizador')
)
ACTION_CHOICE = (
    ('AA', 'Añadir adquisición'),
    ('AR', 'Añadir renta'),
    ('EA', 'Editar adquisición'),
    ('ER', 'Editar renta'),
    ('SA', 'Estatus Activo'),
    ('SI', 'Estatus Inactivo'),
    ('PA', 'Post adquisición'),
    ('PR', 'Post renta'),
    ('RA', 'Respuesta adquisición'),
    ('RR', 'Respuesta renta'),
)

PROPERTY_CHOICE = (
    ('AC', 'Acquisition'),
    ('RT', 'Rent'),
)