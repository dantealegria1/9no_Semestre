AS $1\r\n, COUNT(CASE WHEN d.PositionNumber = 'Doula' AND d.PositionStatusDesc != 'Vacant' THEN 1 END) AS Doula_$1

AS\s+(HomeVisitor_[A-Za-z0-9_]+)