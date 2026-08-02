plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.compose)
}

android {
    namespace = "com.pranav.phone_deck"

    compileSdk {
        version = release(37)
    }

    defaultConfig {
        applicationId = "com.pranav.phone_deck"

        minSdk = 31
        targetSdk = 37

        versionCode = 1
        versionName = "1.0.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            optimization {
                enable = false
            }
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }

    buildFeatures {
        compose = true
    }
}

dependencies {

    // ---------------------------------------------------------
    // Compose BOM
    // ---------------------------------------------------------

    implementation(platform(libs.androidx.compose.bom))

    // ----------------------------------------------------------
    // Navigation
    // ----------------------------------------------------------

    implementation("androidx.navigation:navigation-compose:2.9.3")

    // ---------------------------------------------------------
    // Android Core
    // ---------------------------------------------------------

    implementation(libs.androidx.core.ktx)

    // ---------------------------------------------------------
    // Compose
    // ---------------------------------------------------------

    implementation(libs.androidx.activity.compose)

    implementation(libs.androidx.compose.material3)
    implementation(libs.androidx.compose.material.icons.extended)
    implementation(libs.androidx.compose.ui)
    implementation(libs.androidx.compose.ui.graphics)
    implementation(libs.androidx.compose.ui.tooling.preview)

    // ---------------------------------------------------------
    // Lifecycle
    // ---------------------------------------------------------

    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.9.3")
    implementation("androidx.lifecycle:lifecycle-runtime-compose:2.9.3")
    implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.9.3")

    // ---------------------------------------------------------
    // Coroutines
    // ---------------------------------------------------------

    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.10.2")

    // ---------------------------------------------------------
    // Unit Tests
    // ---------------------------------------------------------

    testImplementation(libs.junit)

    // ---------------------------------------------------------
    // Android Tests
    // ---------------------------------------------------------

    androidTestImplementation(platform(libs.androidx.compose.bom))
    androidTestImplementation(libs.androidx.compose.ui.test.junit4)
    androidTestImplementation(libs.androidx.espresso.core)
    androidTestImplementation(libs.androidx.junit)

    // ---------------------------------------------------------
    // Debug
    // ---------------------------------------------------------

    debugImplementation(libs.androidx.compose.ui.tooling)
    debugImplementation(libs.androidx.compose.ui.test.manifest)
}