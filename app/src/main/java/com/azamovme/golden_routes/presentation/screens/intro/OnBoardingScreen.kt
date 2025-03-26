package com.azamovme.golden_routes.presentation.screens.intro

import android.os.Build
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatDelegate
import androidx.fragment.app.Fragment
import androidx.lifecycle.lifecycleScope
import com.azamovme.golden_routes.R
import com.azamovme.golden_routes.databinding.MotionOnboardingBinding
import com.azamovme.golden_routes.preference.UserDataPreferenceManager
import com.azamovme.golden_routes.themes.LightTheme
import com.azamovme.golden_routes.themes.NightTheme
import com.azamovme.golden_routes.utils.MyAppTheme
import com.dolatkia.animatedThemeManager.AppTheme
import com.dolatkia.animatedThemeManager.Coordinate
import com.dolatkia.animatedThemeManager.ThemeFragment
import com.dolatkia.animatedThemeManager.ThemeManager
import kotlinx.coroutines.launch

class OnBoardingScreen : ThemeFragment() {
    private var _binding: MotionOnboardingBinding? = null
    private val binding get() = _binding!!
    private val userPref by lazy {
        UserDataPreferenceManager(requireContext())
    }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = MotionOnboardingBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        var isDark = userPref.getTheme() == "night"
        binding.themeView.setImageResource(
            if (isDark) R.drawable.light_mode else R.drawable.dark_mode
        )
        binding.themeView.setOnClickListener {
            if (isDark) {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
                userPref.saveTheme("light")
                binding.themeView.setImageResource(R.drawable.dark_mode)
                ThemeManager.instance.changeTheme(LightTheme(), it,400L)
            } else {
                userPref.saveTheme("night")
                binding.themeView.setImageResource(R.drawable.light_mode)
                ThemeManager.instance.changeTheme(
                    NightTheme(),
                    sourceCoordinate = Coordinate((it.x + 40).toInt(), (it.y + 20).toInt()),
                    duration = 400L,
                    isRevers = true
                )
            }
            isDark = !isDark
        }
    }


    @RequiresApi(Build.VERSION_CODES.R)
    override fun syncTheme(appTheme: AppTheme) {
        val myAppTheme = appTheme as MyAppTheme
        context?.let {
            binding.subtitleViewFirst.setTextColor(myAppTheme.fragmentSmallTextColor(it))
            binding.subtitleViewSecond.setTextColor(myAppTheme.fragmentSmallTextColor(it))
            binding.subtitleViewThird.setTextColor(myAppTheme.fragmentSmallTextColor(it))
            binding.root.setBackgroundColor(myAppTheme.fragmentBackgroundColor(it))
            lifecycleScope.launch {
                requireActivity().window.decorView.systemUiVisibility =
                    appTheme.getStatusBarType(requireContext())
                requireActivity().window.navigationBarColor =
                    myAppTheme.statusBarColor(it)
                requireActivity().window.statusBarColor = myAppTheme.statusBarColor(requireContext())

            }
        }

    }
}