package com.azamovme.golden_routes.utils

import android.content.Context
import com.dolatkia.animatedThemeManager.AppTheme


import android.graphics.drawable.Drawable

interface MyAppTheme : AppTheme {

    fun fragmentBackgroundColor(context: Context): Int
    fun activityBottomNavViewBackColor(context: Context): Int
    fun statusBarColor(context: Context): Int
    fun getStatusBarType(context: Context): Int
    fun fragmentLargeTextColor(context: Context): Int
    fun fragmentSmallTextColor(context: Context): Int
    fun fragmentSearchCardColor(context: Context): Int
    fun fragmentCheckboxDrawable(context: Context): Drawable
    fun fragmentBackDrawable(context: Context): Drawable
}