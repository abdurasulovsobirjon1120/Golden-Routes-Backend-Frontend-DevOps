package com.azamovme.golden_routes.presentation.activity

import android.animation.Animator
import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.azamovme.golden_routes.R
import com.azamovme.golden_routes.preference.UserDataPreferenceManager
import com.azamovme.golden_routes.themes.LightTheme
import com.azamovme.golden_routes.themes.NightTheme
import com.azamovme.golden_routes.utils.MainView
import com.azamovme.golden_routes.utils.MyAppTheme
import com.azamovme.golden_routes.utils.initActivity
import com.dolatkia.animatedThemeManager.AppTheme
import com.dolatkia.animatedThemeManager.ThemeActivity
import com.dolatkia.animatedThemeManager.ThemeAnimationListener
import org.koin.android.ext.android.inject

class MainActivity : ThemeActivity(), MainView, ThemeAnimationListener {
    override fun getStartTheme(): AppTheme {
        val pref = UserDataPreferenceManager(this)
        return if (pref.getTheme() == "night") {
            NightTheme()
        } else LightTheme()
    }
//
//    override fun attachBaseContext(newBase: Context?) {
//        LocaleHelper.onAttach(newBase!!)
//        super.attachBaseContext(newBase)
//    }


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
//        initActivity()
    }

    override fun syncTheme(appTheme: AppTheme) {
        val myAppTheme = appTheme as MyAppTheme
//        this.let {
//            // set background color
//            binding.bottomNavView.setBackgroundColor(myAppTheme.activityBottomNavViewBackColor(it))
//        }
    }

    override fun onAnimationCancel(animation: Animator) {
        TODO("Not yet implemented")
    }

    override fun onAnimationEnd(animation: Animator) {
        TODO("Not yet implemented")
    }

    override fun onAnimationRepeat(animation: Animator) {
        TODO("Not yet implemented")
    }

    override fun onAnimationStart(animation: Animator) {
        TODO("Not yet implemented")
    }

    override fun hideBottomBar() {
        TODO("Not yet implemented")
    }

    override fun showBottomBar() {
        TODO("Not yet implemented")
    }

    override fun backPressed() {
        TODO("Not yet implemented")
    }

    override fun restart() {
        TODO("Not yet implemented")
    }
}