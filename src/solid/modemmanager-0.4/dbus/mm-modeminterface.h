/*
 * This file was generated by qdbusxml2cpp version 0.7
 * Command line was: qdbusxml2cpp -N -m -p mm-modeminterface introspection/mm-modem.xml
 *
 * qdbusxml2cpp is Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
 *
 * This is an auto-generated file.
 * Do not edit! All changes made to it will be lost.
 */

#ifndef MM_MODEMINTERFACE_H
#define MM_MODEMINTERFACE_H

#include <QtCore/QObject>
#include <QtCore/QByteArray>
#include <QtCore/QList>
#include <QtCore/QMap>
#include <QtCore/QString>
#include <QtCore/QStringList>
#include <QtCore/QVariant>
#include <QtDBus/QtDBus>

#include "generic-types.h"

/*
 * Proxy class for interface org.freedesktop.ModemManager.Modem
 */
class OrgFreedesktopModemManagerModemInterface: public QDBusAbstractInterface
{
    Q_OBJECT
public:
    static inline const char *staticInterfaceName()
    { return "org.freedesktop.ModemManager.Modem"; }

public:
    OrgFreedesktopModemManagerModemInterface(const QString &service, const QString &path, const QDBusConnection &connection, QObject *parent = 0);

    ~OrgFreedesktopModemManagerModemInterface();

    Q_PROPERTY(QString Device READ device)
    inline QString device() const
    { return qvariant_cast< QString >(property("Device")); }

    Q_PROPERTY(QString Driver READ driver)
    inline QString driver() const
    { return qvariant_cast< QString >(property("Driver")); }

    Q_PROPERTY(bool Enabled READ enabled)
    inline bool enabled() const
    { return qvariant_cast< bool >(property("Enabled")); }

    Q_PROPERTY(uint IpMethod READ ipMethod)
    inline uint ipMethod() const
    { return qvariant_cast< uint >(property("IpMethod")); }

    Q_PROPERTY(QString MasterDevice READ masterDevice)
    inline QString masterDevice() const
    { return qvariant_cast< QString >(property("MasterDevice")); }

    Q_PROPERTY(uint Type READ type)
    inline uint type() const
    { return qvariant_cast< uint >(property("Type")); }

    Q_PROPERTY(QString UnlockRequired READ unlockRequired)
    inline QString unlockRequired() const
    { return qvariant_cast< QString >(property("UnlockRequired")); }

public Q_SLOTS: // METHODS
    inline QDBusPendingReply<> Connect(const QString &number)
    {
        QList<QVariant> argumentList;
        argumentList << qVariantFromValue(number);
        return asyncCallWithArgumentList(QLatin1String("Connect"), argumentList);
    }

    inline QDBusPendingReply<> Disconnect()
    {
        QList<QVariant> argumentList;
        return asyncCallWithArgumentList(QLatin1String("Disconnect"), argumentList);
    }

    inline QDBusPendingReply<> Enable(bool enable)
    {
        QList<QVariant> argumentList;
        argumentList << qVariantFromValue(enable);
        return asyncCallWithArgumentList(QLatin1String("Enable"), argumentList);
    }

    inline QDBusPendingReply<Ip4ConfigType> GetIP4Config()
    {
        QList<QVariant> argumentList;
        return asyncCallWithArgumentList(QLatin1String("GetIP4Config"), argumentList);
    }

    inline QDBusPendingReply<InfoType> GetInfo()
    {
        QList<QVariant> argumentList;
        return asyncCallWithArgumentList(QLatin1String("GetInfo"), argumentList);
    }

Q_SIGNALS: // SIGNALS
};

#endif
