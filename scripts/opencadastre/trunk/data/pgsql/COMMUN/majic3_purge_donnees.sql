﻿-- PURGE DES DONNEES : DEBUT;
-- Purge des tables de données;
DELETE FROM [PREFIXE]voie WHERE lot='[LOT]';
DELETE FROM [PREFIXE]commune WHERE lot='[LOT]';
DELETE FROM [PREFIXE]lotslocaux WHERE lot='[LOT]';
DELETE FROM [PREFIXE]lots WHERE lot='[LOT]';
DELETE FROM [PREFIXE]parcellecomposante WHERE lot='[LOT]';
DELETE FROM [PREFIXE]pdl WHERE lot='[LOT]';
DELETE FROM [PREFIXE]comptecommunal WHERE lot='[LOT]';
DELETE FROM [PREFIXE]proprietaire WHERE lot='[LOT]';
DELETE FROM [PREFIXE]pevdependances WHERE lot='[LOT]';
DELETE FROM [PREFIXE]pevprofessionnelle WHERE lot='[LOT]';
DELETE FROM [PREFIXE]pevprincipale WHERE lot='[LOT]';
DELETE FROM [PREFIXE]pevtaxation WHERE lot='[LOT]';
DELETE FROM [PREFIXE]pevexoneration WHERE lot='[LOT]';
DELETE FROM [PREFIXE]pev WHERE lot='[LOT]';
DELETE FROM [PREFIXE]local10 WHERE lot='[LOT]';
DELETE FROM [PREFIXE]local00 WHERE lot='[LOT]';
DELETE FROM [PREFIXE]suftaxation WHERE lot='[LOT]';
DELETE FROM [PREFIXE]sufexoneration WHERE lot='[LOT]';
DELETE FROM [PREFIXE]suf WHERE lot='[LOT]';
DELETE FROM [PREFIXE]parcelle WHERE lot='[LOT]';
-- PURGE DES DONNEES : FIN;