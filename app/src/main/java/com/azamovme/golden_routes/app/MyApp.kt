package com.azamovme.golden_routes.app

import android.app.Application
import org.koin.android.ext.koin.androidContext
import org.koin.android.ext.koin.androidLogger
import org.koin.core.context.startKoin
import org.koin.core.logger.Level

class MyApp: Application() {

    companion object {
        lateinit var instance: MyApp
    }

    override fun onCreate() {
        super.onCreate()
        instance= this
        startKoin {
            androidLogger(Level.ERROR)
            androidContext(this@MyApp)
//            modules(listOf(NetworkModule))
        }

//        MapKitFactory.setApiKey("60e43975-7ee9-4a3d-bb53-a16f284f0395")
    }
}