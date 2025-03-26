package com.azamovme.golden_routes.preference

import android.content.Context
import android.preference.PreferenceManager

class UserDataPreferenceManager(private val context: Context) {
    private val prefs = PreferenceManager.getDefaultSharedPreferences(context)

    fun saveTheme(token: String) {
        prefs.edit().putString("theme", token).apply()
    }


    fun getTheme(): String? {
        return prefs.getString("theme", null)
    }
    fun saveToken(token: String) {
        prefs.edit().putString("token", token).apply()
    }


    fun getToken(): String? {


        return prefs.getString("_token", null)
    }

    enum class Language(val code: String) {
        RUSSIAN("ru"), UZBEK("la"), KRILL("uz")
    }

    fun setLanguage(language: Language) {
        prefs.edit().putString("language", language.code).apply()
    }

    fun getLanguage(): Language {
        val sharedPreferences =
            androidx.preference.PreferenceManager.getDefaultSharedPreferences(context)
        return when (sharedPreferences.getString("language", "uz")) {
            "la" -> {
                Language.UZBEK
            }

            "ru" -> {
                Language.RUSSIAN
            }

            else -> {
                Language.KRILL
            }
        }
    }

}